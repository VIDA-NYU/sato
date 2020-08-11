import click
import pandas as pd

from sato.predict import evaluate


@click.command('predict')
@click.option(
    '-n', '--count',
    default=1000,
    help='Sample size'
)
@click.argument(
    'src',
    nargs=-1,
    type=click.Path(file_okay=True, dir_okay=False, exists=True)
)
def run_predict(count, src):
    """Predict column types for tab-delimited CSV file(s)."""
    for filename in src:
        try:
            df = pd.read_csv(
                filename,
                delimiter='\t',
                compression='gzip',
                low_memory=False
            )
            rows = df.shape[0]
            if rows > 0:
                if rows > count:
                    df = df.sample(n=count, random_state=1)
                labels = evaluate(df)
                print(filename)
                for i in range(len(df.columns)):
                    print('%s\t%s' % (df.columns[i], labels[i]))
        except Exception as ex:
            print('error {}'.format(ex))


@click.group()
def cli():  # pragma: no cover
    """Command line interface for SATO."""
    pass


cli.add_command(run_predict)
