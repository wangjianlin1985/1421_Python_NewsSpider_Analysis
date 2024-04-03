# coding: utf-8
__author__ = 'ila'
import json
from dj2.settings import spark,jdbc_url

def spark_read_mysql(sql,json_filename):
    df = spark.read.format("jdbc").options(url=jdbc_url,
                                           dbtable=sql).load()
    count = df.count()
    df_data = df.toPandas().to_dict()
    json_data = []
    for i in range(count):
        temp = {}
        for k, v in df_data.items():
            temp[k] = v.get(i)
        json_data.append(temp)
    with open(json_filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(json_data, indent=4, ensure_ascii=False))