#!/usr/bin/env python
# coding: utf-8

from minicms.wsgi import *
from news.models import Column, Article


def main():
    columns_urls = [
        ('体育新闻', 'sports', '包含体NBA,CBA,英超,意甲,西甲,冠军杯,福彩,网球,F1,棋牌,乒羽,综合体育等'),
        ('社会新闻', 'society', '全面展现社会万象、法治聚焦、奇闻异事等社会资讯,报道最前沿、鲜活的社会新闻。'),
        ('科技新闻', 'tech', '互联网、IT业界、通信、趋势、科技访谈等'),
    ]

    for column_name, url, valu, in columns_urls:
        c = Column.objects.get_or_create(
            name=column_name, slug=url, intro=valu)[0]

        # 创建 10 篇新闻
        for i in range(1, 11):
            article = Article.objects.get_or_create(
                title='{}_{}'.format(column_name, i),
                slug='article_{}'.format(i),
                content='新闻详细内容：{}{}'.format(column_name, i)
            )[0]
            article.column.add(c)

if __name__ == '__main__':
    main()
    print("Done!")
