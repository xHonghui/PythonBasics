import re
import threading
from Log import log
import requests
import pandas as pd
import json
import time
from conf import engine


class Crawl:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}

    def page_parse(self, kind,base_link,kind_number,total_page):
        try:
            for j in range(1,int(total_page)+1):
                link='{0}t{1}c{2}/'.format(base_link,kind_number,j)
                print('=>',link)
                content=requests.get(link,headers=self.headers).content.decode()
                response=re.sub('\s','',content)
                houselist=re.findall('<divclass="houseList">(.*?)</div><divclass="houserightSide">',response)
                everyone=re.findall('<liclass="hosueLi">(.*?)</li>',houselist[0])
                values=[]
                columns=['类型名称','楼盘名称','链接','行政区','商圈','在租套数','租赁面积m2','最低价格元月起']
                for i in everyone:
                    info=re.findall('<divclass="showInfo">(.*?)<\/div>',i)
                    try:
                        name=re.findall('<a[^>]*>(.*?)</a>',info[0])[0]#名称
                    except:
                        name='--'
                    try:
                        name_link=re.findall('<ahref="(.*?)"target',info[0])[0] # 链接
                        name_link='http://www.omiaozu.com'+name_link
                    except:
                        name_link='--'
                    try:
                        district = re.findall('<font[^>]*>(.*?)</font>', info[0])[0]  # 位置
                    except:
                        district='--'
                    try:
                        circle = re.findall('<font[^>]*>(.*?)</font>', info[0])[1]  # 商圈
                    except:
                        circle='--'
                    try:
                        number=re.findall('<spanclass="ibuilding">(.*?)<\/span>',i)[0]#当前在租套数
                    except:
                        number='--'
                    try:
                        area=re.findall('<spanclass="iarea">(.*?)<\/span>',i)[0]#出租户型m2
                    except:
                        area='--'
                    try:
                        price_list=re.findall('<pclass="houseUnit"><span>(.*?)<\/span>',houselist[0])#最低价格128元/m².月起
                        low_price=price_list[everyone.index(i)]
                    except:
                        low_price='--'
                    values.append([kind,name,name_link,district,circle,number,area,low_price])
                self.create_table('miao_zu_data',columns, values)
        except Exception as e:
            log.info(e,exc_info=True)


    def get_content(self):
        try:
            resp = requests.get(self.url, headers=self.headers).content.decode()
            response = re.sub('\s', '', resp)
            banner = re.findall('<ulclass="filterListclearfix">(.*?)</ul>', response)  # 总分类
            href_list=re.findall('<ahref="/sz/xiezilou/t(\d+)/"',banner[0])
            list_name=re.findall('<a[^>]*>(.*?)<\/a>',banner[0])
            thd_list=[]
            for i in href_list:
                kind=list_name[href_list.index(i)+1]
                base='http://www.omiaozu.com/sz/xiezilou/'
                url=base+'t{0}/'.format(i)
                print(url)
                resp = requests.get(url, headers=self.headers)
                response = resp.content.decode()
                response = re.sub('\s', '', response)
                try:
                    total_page = re.findall('data-totalPage="(\d+)"', response)[0]
                except:
                    total_page = 0
                print('[-]总页数:',total_page)
                t=threading.Thread(target=self.page_parse,args=(kind,base,i,total_page))
                t.start()
                thd_list.append(t)
            for thd in thd_list:
                thd.join()
        except Exception as e:
            log.info(e,exc_info=True)
    def get_detail_page(self,name,url):
        session=requests.session()
        session.headers=self.headers
        resp=session.get(url).content.decode()
        response = re.sub('\s', '', resp)
        build_id=re.findall('"id"type="hidden"value="(.*?)">',response)[0]
        link='http://www.omiaozu.com/rest/house/selectHouseToBuildDetail?buildId={0}&areaRange=&change=1000&priceRange=&orderColumn=&isDesc='.format(build_id)
        json_str=session.get(link).content
        resp_json=json.loads(json_str)
        data=resp_json['houseList']
        values=[]
        columns=['楼盘名称','面积','单价','装修','楼层','可纳工位']
        for d in data:
            values.append([name,d['area'],(d['showPrice']+d['houseUnitsName']),d['decorationTypeName'],d['showFloor'],
                           (d['minSeat']+'-'+d['maxSeat'])])
        self.create_table('miao_zu_detial',columns, values)
    def create_table(self, tablename,columns, values):
        try:
            my_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            cmd = 'CREATE TABLE {0}(rid INT Primary KEY AUTO_INCREMENT);'.format(tablename)
            try:
                engine.execute(cmd)
                print('[-]create table', tablename)
            except:
                pass
            # 对比增加列
            table_column = '''select column_name from information_schema.COLUMNS where table_name="{0}"'''.format(
                tablename)
            row = []
            for i in engine.execute(table_column):
                row.append(re.findall('\'(.*?)\',', str(i))[0])
            columns.append('更新时间')
            for k in values:
                k.append(my_time)
            for i in columns:
                if i not in row:
                    cmd = 'alter table {0} add column {1} TEXT'.format(str(tablename), str(i))
                    engine.execute(cmd)
            df = pd.DataFrame(data=values, columns=columns)
            df.to_sql(name=tablename, con=engine, if_exists='append', index=False)
            print(df)
        except Exception as e:
            log.info(e,exc_info=True)





if __name__ == '__main__':
    crawl = Crawl('http://www.omiaozu.com/sz/listing//')
    crawl.get_content()
    conn = engine.connect()
    build_name = conn.execute('select 楼盘名称 from miao_zu_data').fetchall()
    build_id = conn.execute('select 链接 from miao_zu_data').fetchall()
    for name in build_name:
        crawl.get_detail_page(name,build_id[build_name.index[name]])







