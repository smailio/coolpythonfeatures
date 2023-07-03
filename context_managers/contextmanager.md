# Les context managers

###### Un code trés commun
```python
def truc():
    print("machin")

print("Avant")
try:
    truc()
finally:
    print("Après")
```

Si on se retrouve à ré-écrire tout le temps print("Avant") et print("Aprés")
ça peut valoir le coup de factoriser ce code. 

###### Bon OK, on peu résoudre ça avec des décorateurs

```python
def printAvantApres(f):
    print("Avant")
    try:
        f()
    finally:
        print("Aprés")

@printAvantApres
def truc():
    print("machin")
```

Le truc c'est que des fois on aimerait bien ne pas enrober notre code dans une fonction 
juste pour pouvoir la décorer. Vous imaginez à chaque fois qu'on lit un fichier ? 

```python
def inject_config_file(f):
    file = open('config_file_path')
    try:
        f(file)
    finally:
        file.close()
    
    
@inject_config_file
def do_stuff(config_file):
    print(config_file)
```

En Python y a le keyword *with* si vous avez déjà ouvert un fichier en Python j'espere que vous 
l'avez fait comme ça : 

```python
with open('config_file_path') as f:
    print(f)
```

- open se comporte à la foic comme une fonction et comme un *context manager*
- au début du bloc il ouvre un fichier qui devient accessible à travers la variable f
- à la fin du bloc il ferme le fichier, peu importe ce qu'il s'est passé dans le bloc,
càd que si une exception a été levée le fichier sera quand même fermé 

Un context manager est une abstraction sur le try finally. 

Heuresement qu'on ce keyword, en Python si on avait juste la fonction les dev 
auraient la flemme de fait un try finally, et encore plus la flemme 
d'enrober leur code dans des fonctions et d'utiliser les décorateurs,
on vivrait dans un monde où les ressources ne sont jamais fermés et la qualité moyenne des 
codes  serait bien plus basse qu'elle ne l'est aujourd'hui.     

 

##### Un contexte manager ressemble à ça 

```python
class MonSuperContextManager:
    def __enter__(self):
        print("Avant")
        
    def __exit__(self, type, value, traceback):
        # faites pas attention aux paramètres, ce sont toutes les infos
        # automatiquement passées à __exit__ et qui servent pour inspecter
        # une éventuelle exception
        print("Après")

with MonSuperContextManager():
    print("Faire des trucs")
```
Affiche 

```
Avant
Faire des trucs
Après
```

- MonSuperContextManager enrobe un bloc de code
- avant d'éxécuter le bloc de code enrobé Python appel __enter__
- aprés avoir éxécuter le bloc de code enrobé Python appel __exit__