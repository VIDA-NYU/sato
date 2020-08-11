import click
import pandas as pd

from sato.predict import evaluate


@click.command('run')
@click.option(
    '-n', '--count',
    default=1000,
    help='Sample size'
)
@click.argument(
    'filename',
    type=click.Path(file_okay=True, exists=True)
)
def run_sato(count, filename):
    """Run SATO on tab-delimited Socrata file."""
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
            for i in range(len(df.columns)):
                print('%s\t%s' % (df.columns[i], labels[i]))
    except Exception as ex:
        print('error {}'.format(ex))


@click.group()
def cli():  # pragma: no cover
    """Command line interface for SATO."""
    pass


cli.add_command(run_sato)
