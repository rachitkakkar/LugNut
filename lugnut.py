from markdown import markdown as md
import sys

file_path = sys.argv[1]
print(f'- Generating Html Into {sys.argv[2]}')

html = '''
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300italic,700,700italic">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/milligram/1.4.1/milligram.css">

<style>
    body {
        width: 35em;
        margin: 0 auto;
        /*font-family: Tahoma, Verdana, Arial, sans-serif;*/
    }
</style>

''' + md(open(sys.argv[1]).read())

output = open(sys.argv[2], 'w')
output.write(html)

print('Done!')
print('LugNut was made by Rachit Kakkar')
