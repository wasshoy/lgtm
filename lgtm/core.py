import click


@click.command()
@click.option('--message', '-m', default='LGTM',
              show_default=True, help='画像に乗せる文字列')  # キーワード引数
@click.argument('keyword')  # 位置引数
def cli(keyword, message):
    """LGTM画像生成ツール"""
    lgtm(keyword, message)
    click.echo('lgtm')  # 動作確認用


def lgtm(keyword, message):
    pass
