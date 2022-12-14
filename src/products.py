from datetime import datetime

class Product:

    autoplanet_category_dic = {
        "CATEGORIA04": "Correa de Accesorios y Servicios",
        "114": "Suspensión y Dirección",
        "113": "Sistema de Escape",
        "112": "Sistema de Alimentación",
        "111": "Sensores y Eléctrica",
        "110": "Rodamiento y Retenes",
        "109": "Refrigeración y Calefacción",
        "108": "Motor de Partida y Alternador",
        "107": "Motor",
        "106": "Frenos",
        "105": "Filtros",
        "104": "Embragues y Transmisión",
        "103": "Distribución",
        "102": "Carrocería",
        "101": "Cambio de Aceite",
        "100": "Afinamiento y Encendido",
        "12": "Mantenimiento",
        "11": "oportunidades",
        "10": "Exclusivos Web",
        "09": "Desabolladura y Pintura",
        "08": "Herramientas",
        "07": "Limpieza y Cuidado",
        "06": "Accesorios",
        "05": "Iluminación y Electricidad",
        "04": "Neumáticos",
        "03": "Lubricantes",
        "02": "Baterías",
        "01": "Repuestos"}

    def __init__(self, name, product_id, brand, description, sku, image_at, price, url, specifications, store, category, scrap_date=None) -> None:
        self.name = name
        self.store_product_id = product_id
        self.brand = brand
        if not scrap_date:
            self.scrap_date = datetime.date(datetime.today())
        else:
            self.scrap_date = scrap_date
        self.description = description
        self.sku = sku
        self.image_at = image_at
        self.price = price
        self.url = url
        # specifications = {item1_key: item1_value, ..., itemn_key: itemn_value}
        self.specifications = specifications
        self.store = store
        self.category = category

    # Agregar Categoría

    def __repr__(self):
        return f"{self.name}: ${self.price}"

    @staticmethod
    def clean(string):
        string = str(string)
        # If there is a ; remove everything else
        clean_string = string.split(";")[0]
        stripped_string = clean_string.strip()
        return stripped_string

    @staticmethod
    # Todo con RegEx
    def untilde(string):
        simplified_string = string.replace(
            "Á", "A").replace(
                "Í", "I").replace(
                    "É", "E").replace(
                        "Ú", "U").replace(
                            "Ó", "O").replace(
                                "Ñ", "NI").replace(
                                    " ", "_").replace(
                                        "-", "_").replace(
                                            "/", "Y").replace(
                                                ".", "PUNTO").replace(
                                                    "(", "__").replace(")", "__")
        return simplified_string

    def join_category(self, category):
        match self.store:
            case "autoplanet":
                category = Product.autoplanet_category_dic[category]
            case "sodimac":
                category = category.split("/")[1]
            case "easy":
                pass
        category = category.upper()
        category = self.untilde(category)
        return category


    @staticmethod
    def crop(string):
        if len(string) > 255:
            return f"{string[0:250]}..."
        else: return string

    def export_dict(self):
        atribute_json = {
            "NAME": self.crop(self.clean(self.name)),
            "STORE_PRODUCT_ID": self.clean((self.store_product_id)),
            "BRAND": self.crop(self.clean(self.brand)),
            "DATE": self.scrap_date,
            "DESCRIPTION": self.clean(self.description),
            "SKU": self.clean((self.sku)),
            "URL": self.clean(self.url),
            "IMAGE_AT": self.crop(self.clean(self.image_at)),
            "PRICE": int(self.price),
            "STORE": self.crop(self.clean(self.store)),
            "CATEGORY": self.join_category(self.category)
        }
        # Update the atributes dict with the specs as attributes to be uploaded to DF
        # We want the keys to be in uppercase
        if self.specifications:
            specs = dict(zip(
                map(
                    lambda key: self.untilde(self.clean(key).upper()), self.specifications.keys()
                ), 
                map(
                    lambda value: self.crop(self.clean(value)), self.specifications.values()
                )))
            atribute_json.update(specs)
        return atribute_json


if __name__ == "__main__":
    import sodimac.product_getter as sodimac_getter
    import easy.product_getter as easy_getter

    # product_data = sodimac_getter.parse_data(sodimac_getter.get_data_for(110316112))
    # bateria = Product(**product_data)

    # product_data = easy_getter.parse_data(easy_getter.get_data_for(672286), 672286)
    # anti_pinchazo = Product(**product_data)

    # print(bateria.export_dict())
    # print(anti_pinchazo.export_dict())



