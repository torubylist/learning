#  -*- coding: utf-8 -*-
# arg_test.py

import argparse
import click

#def counter(file_type=None):
#    return {file_type: 100}

@click.command()
@click.option("-f", "--file", help='统计制定文件类型')
def counter(file=None):
    click.echo({file: 100})

#parser = argparse.ArgumentParser()
#
#parser.add_argument("-f", "--file", help="统计制定文件类型")

#args = parser.parse_args()
#print(counter(args.file))

if __name__ == '__main__':
    print(counter())
