from mitreattack.navlayers import Layer, ToExcel, ToSvg

layer = Layer()
layer.from_file("data/layers/example_layer.json")

print(f'Name: {layer.layer.name}')
print(f'Description: {layer.layer.description}')

svg = ToSvg(domain=layer.layer.domain, source='local', resource="data/stix_data/enterprise-attack.json")
svg.to_svg(layer, filepath="data/layers/example.svg")

excel = ToExcel(domain='enterprise', source='local', resource="data/stix_data/enterprise-attack.json")
excel.to_xlsx(layerInit=layer, filepath="data/layers/example_layer.xlsx")
