# -*- coding: utf-8 -*-
"""Main module."""

import codecs as cs
import os
from glob import glob

import click
import pandas as pd
from tqdm import tqdm


def txt2csv(txt, output):
    with cs.open(txt,'r', 'gbk') as f:
        fl = f.readlines()

    del fl[0]
    del fl[0]
    del fl[-1]

    if not os.path.isdir(output):
        os.mkdir(output)

    csv = os.path.split(txt)
    csv = csv[1].replace('.txt', '.csv')
    csv = os.path.join(output, csv)
    
    with open(csv, 'w') as fp:
        fp.writelines(fl)

    df = pd.read_csv(csv, names=['Date','Open','High','Low','Close','Volume','Amount'])
    df.to_csv(csv, index=False)

@click.command(help=u'通达信数据转换程序.')
@click.option('-i', '--input', default=os.path.expanduser("./input"), type=click.Path(file_okay=False), help=u'历史数据下载目录, 默认当前目录下 input')
@click.option('-o', '--output', default=os.path.expanduser("./output"), type=click.Path(file_okay=False), help=u'转换后输出目录, 默认当前目录下 output')
def main(input, output):
    files = glob('%s/*.txt' % input.rstrip('/'))
    for txt in tqdm(files):
        txt2csv(txt, output)


if __name__ == '__main__':
    main()
