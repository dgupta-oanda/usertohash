import click
import csv
import hashlib

@click.command()
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.File('w'))
def makeitso(input, output):
    """Takes INPUT file CSV and outputs a CSV with hashed names\n
    INPUT file is a CSV file with a single column, the first row is a header with the column name\n
    OUTPUT file is a CSV file with a single column, the first row is a header with the same column name as input\n
    OUTPUT file's rows will contain a SHA-256 hash of every row of input\n
    """
    reader = csv.reader(input)
    writer = csv.writer(output)
    writer.writerow(reader.__next__())
    for row in reader:
        username = row[0]
        hashed = hashlib.sha256(username.encode('utf-8')).hexdigest()
        writer.writerow([hashed])
    
if __name__ == '__main__':
    makeitso()
