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
    """Predict column types for CSV file(s)."""
    for filename in src:
        # This is a very basic attempt to determine the file compression and
        # delimiter from the suffix. Currently, the following four oprions are
        # recognized: '.csv', '.csv.gz', '.tsv', '.tsv.gz'. Files ending with
        # '.gz' are assumed to be compressed by 'gzip' all other files are
        # considered as uncompressed. The delimiter for '.csv' files is ',' and
        # for '.tsv' files the delimiter is '\t'.
        if filename.endswith('.csv'):
            compression = None
            delimiter = ','
        elif filename.endswith('.csv.gz'):
            compression = 'gzip'
            delimiter = ','
        elif filename.endswith('.tsv'):
            compression = None
            delimiter = '\t'
        elif filename.endswith('.tsv.gz'):
            compression = 'gzip'
            delimiter = '\t'
        else:
            raise ValueError('unrecognized file format')
        try:
            df = pd.read_csv(
                filename,
                delimiter=delimiter,
                compression=compression,
                low_memory=False
            )
            rows = df.shape[0]
            print('\n{}'.format(filename))
            print('{}'.format('-' * len(filename)))
            if rows == 0:
                # Skip empty files.
                continue
            if rows > count:
                # Take sample for large files.
                df = df.sample(n=count, random_state=1)
            # Evaluate data frame to get predicted coluumn labels.
            labels = evaluate(df)
            for i in range(len(df.columns)):
                print('%s: %s' % (df.columns[i], labels[i]))
        except Exception as ex:
            print('error {}'.format(ex))


@click.group()
def cli():  # pragma: no cover
    """Command line interface for SATO."""
    pass


cli.add_command(run_predict)
