#!/usr/bin/env python3
import tomllib

recipe_file = 'recipes/recipe.toml'
tex_file = 'sections/cocktails.tex'
# load toml file
with open(recipe_file, 'rb') as f:
    data = tomllib.load(f) # data is a dict

begin_group = "\\begin{Group}{cocktail}"
end_group = "\\end{Group}"
def generate_latex(data):
    with open(tex_file, 'w') as f:
        f.write(begin_group)
        for i, cocktail in enumerate(data['cocktails']):
            f.write('\n')
            f.write('\\Entry{' + cocktail['name_cn'] + ' ' + cocktail['name_en'].replace('&', '\\&') + '}{\\textyen ' + str(cocktail['price']) + '}\n')
            f.write('\\Recipecn{' + '、'.join(cocktail['menu']['ingredients_cn']) + '}\n')
            f.write('\\Recipeen{' + ', '.join(cocktail['menu']['ingredients']) + '}\n')
            f.write('\\Expl{' + cocktail['menu']['description'] + '}\n')
            if (i + 1) % 4 == 0 and i != len(data['cocktails']) - 1:
                f.write(end_group)
                f.write('\n')
                f.write(begin_group)
        f.write(end_group)
        f.write('\n')

# if main
if __name__ == '__main__':
    generate_latex(data)