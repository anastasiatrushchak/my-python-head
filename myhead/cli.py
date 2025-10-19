import click
import sys

@click.command()
@click.option(
    '-n', '--lines', 'lines', 
    type=int, 
    default=10, 
    help='Вивести перші K рядків. За замовчуванням 10.',
    show_default=True
)
@click.option(
    '-c', '--bytes', 'byte_count', 
    type=int, 
    help='Вивести перші K байтів. Цей параметр має вищий пріоритет, ніж --lines.'
)
@click.argument(
    'file', 
    type=click.Path(exists=True, dir_okay=False, allow_dash=True), 
    default='-'
)
def main(lines, byte_count, file):
   
    try:
        if byte_count is not None:
            if file == '-':
                data = sys.stdin.buffer.read(byte_count)
            else:
                with open(file, 'rb') as f:
                    data = f.read(byte_count)
            sys.stdout.buffer.write(data)
        
        else:
            input_stream = None
            if file == '-':
                input_stream = sys.stdin
            else:
                input_stream = open(file, 'r', encoding='utf-8')
            
            with input_stream as f:
                for i, line in enumerate(f):
                    if i >= lines:
                        break
                    sys.stdout.write(line)
                    
    except FileNotFoundError:
        sys.stderr.write(f"myhead: неможливо відкрити '{file}' для читання: Файл не знайдено\n")
        sys.exit(1)
    except Exception as e:
        sys.stderr.write(f"myhead: Помилка: {e}\n")
        sys.exit(1)

if __name__ == '__main__':
    main()