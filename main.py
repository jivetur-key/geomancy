#!/usr/bin/python
import generate, name_key, geo_display

def main():
    g = generate.Generate()
    g._generate()
    name = name_key.Name_key(g.geo)
    name._name_key()
    app = geo_display.Geo_display(g.geo, name.name_list)
    app.on_execute()

if __name__ == '__main__':
    main()
