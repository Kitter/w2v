# coding:utf-8


import os
import click

from build import build_corpus, build_word2vec


@click.group()
def cli():
    pass


@click.group()
def build():
    pass


@build.command(help="build corpus from target textfile")
@click.argument("target", type=click.Path())
@click.argument("corpus", type=click.Path())
def corpus(target, corpus):
    build_corpus(target, corpus)


@build.command(help="build word2vec from corpus")
@click.argument("corpus", type=click.Path())
@click.argument("word2vec", type=click.Path())
def word2vec(corpus, word2vec):
    build_word2vec(corpus, word2vec)


@cli.command(help="interactive shell with Word2Vec instance")
@click.argument("word2vec", type=click.Path())
def shell(word2vec):
    profile =  __file__
    profile = "/".join(profile.split("/")[0:0-1])
    profile = profile + "/.profile_ipython"
    print profile
    os.environ["WORD2VEC_PATH"] = word2vec
    os.system("ipython --profile-dir={}".format(profile))


cli.add_command(build)


if __name__ == "__main__":
    cli(obj={})
