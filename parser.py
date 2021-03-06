import xml.etree.ElementTree as ET
from models_menu import *


class Parser:
    def __init__(self, file_path):
        self.file_path = file_path
        tree = ET.parse(file_path)
        self.root = tree.getroot()
        for child in self.root:
            if child.tag == 'meta':
                self.meta = child

    def get_all_data(self):

        lst = []
        for data in self.root.findall('data'):
            lst.append(self.process_data_tag(data))

        return lst

    def process_data_tag(self, data):
        try:
            id_data = data.find('id').text
            name_data = data.find('name').text
            slug = data.find('slug').text
            description = data.find('description').text
            updated_at = data.find('updated_at').text
            created_at = data.find('created_at').text
        except Exception as exp:
            print('get_data() :: Got expcetion: %s' % exp)
            pass
        dispensary = []
        subcategory = []
        category = []
        units = []
        images = []
        logo = []

        for child in data:

            if child.tag == 'dispensary':
                id = child.find('id').text
                name = child.find('name').text
                dispensary.append(Dispensary(id, name))

            # getting <category.xml> from data
            if child.tag == 'subcategory':
                id = child.find('id').text
                name = child.find('name').text
                subcategory.append(SubCategory(id, name))

            # getting <category.xml> from data
            if child.tag == 'category.xml':
                id = child.find('id').text
                name = child.find('name').text
                category.append(Category(id, name))

            if child.tag == 'units':
                for data_tag in child:
                    id = data_tag.find('id').text
                    name = data_tag.find('name').text
                    key = data_tag.find('key').text
                    value = data_tag.find('value').text
                    units.append(Unit(id, name, key, value))

            # getting <images> from data

            if child.tag == 'images':

                for data_tag in child:
                    id = data_tag.find('id').text
                    name = data_tag.find('name').text
                    thumb = data_tag.find('thumb').text
                    aspectRatio = data_tag.find('aspectRatio').text
                    listing_medium = data_tag.find('listing_medium').text
                    listing_small = data_tag.find('listing_small').text
                    listing_large = data_tag.find('listing_large').text
                    square_medium = data_tag.find('square_medium').text
                    square_small = data_tag.find('square_small').text
                    square_large = data_tag.find('square_large').text
                    images.append(Image(id, name, thumb, aspectRatio,
                                        listing_medium, listing_small,
                                        listing_large, square_medium,
                                        square_small, square_large))

            # getting <logo> from data
            if child.tag == 'logo':
                for data_tag in child:
                    id = data_tag.find('id').text
                    name = data_tag.find('name').text
                    thumb = data_tag.find('thumb').text
                    aspectRatio = data_tag.find('aspectRatio').text
                    listing_medium = data_tag.find('listing_medium').text
                    listing_small = data_tag.find('listing_small').text
                    listing_large = data_tag.find('listing_large').text
                    square_medium = data_tag.find('square_medium').text
                    square_small = data_tag.find('square_small').text
                    square_large = data_tag.find('square_large').text
                    logo.append(Logo(id, name, thumb, aspectRatio,
                                     listing_medium, listing_small,
                                     listing_large, square_medium,
                                     square_small, square_large))

        return Data(id_data, name_data, slug, dispensary, description,
                    subcategory, category, units, images,
                    updated_at, created_at, logo)

    def get_meta_data(self):
        for data in self.meta:
            total = data.find('total').text
            count = data.find('count').text
            per_page = data.find('per_page').text
            current_page = data.find('current_page').text
            total_pages = data.find('total_pages').text
            links = []

            for child in data:
                if child.tag == 'links':
                    # next = child.find('next').text
                    links.append(Links(next))

        return Meta_Data(total, count, per_page,
                         current_page, total_pages, links)

    def get_meta_data_all(self):
        for data in self.meta:
            total = data.find('total').text
            count = data.find('count').text
            per_page = data.find('per_page').text
            current_page = data.find('current_page').text
            total_pages = data.find('total_pages').text
            links = []

            for child in data:
                if child.tag == 'links':
                    previous = child.find('previous').text
                    links.append(Links_cat(previous))

        return Meta_Data_cat(total, count, per_page,
                             current_page, total_pages, links)

        return Meta_Data(total, count, per_page,
                         current_page, total_pages)


def get_parser_data():
    parser = Parser('latest.xml')

    Data = []
    for data in parser.get_all_data():
        print '', data.id
        print '', data.name
        print '', data.description
    # return [Data for data in parser.get_all_data()]


def get_all_products():
    parser = Parser('latest.xml')

    return parser.get_all_data()


def get_category():
    parser = Parser('latest.xml')
    try:
        # print '+++++++++++++++++++++++++++++++'
        # for pro in parser.get_all_data():
        #     #if product.subcategory == subcategory:
        #     print "====================", pro
        return [pro for pro in parser.get_all_data()]
    except:
        pass


# get prerolls category
def get_prerolls(name):
    name_lst = []
    prsr = Parser('latest.xml')
    for cat in prsr.get_all_data():
        print "=========", cat.slug
        print '-----111---------'
        for child in cat.subcategory:
            print '------22222------', child.name
            if child.name == name:
                print '-----3333-----'
                print '------444444------', cat.name
                name_lst.append(cat.name)
    return name_lst




# def get_products_by_category(category, subcategory):
#     pp = ProductParser('products.xml')
#
#     return [product for product in pp.get_products()
#             if product.category == category and
#             product.subcategory == subcategory]


if __name__ == '__main__':
    # parser = Parser('latest.xml')
    # category.xml is not a proper format so it will not parse
    #
    #
    #
    #
    # category xml :: parsering
    print 'category xml :: parsering..'
    # parser = Parser('category.xml')
    # get_data = parser.get_all_data()
    # for data in get_data:
    #     data.show_data_details()
    # meta = parser.get_meta_data()
    # meta.show_meta_details()

    # dispensary xml :: parsering
    print 'dispensary xml :: parsering..'
    prsr = Parser('latest.xml')
    get_data = prsr.get_all_data()
    for data in get_data:
        data.show_data_details()
    # meta = parser.get_meta_data()
    # meta.show_meta_details()

    # xml sending my mail (categories.xml)
    # parser = Parser('categories.xml')

    # only for category and dispensary(both) xml
    # print '(Both) :: category and dispensary xml'
    # parser = Parser('both(cat&dis).xml')
    # meta = parser.get_meta_data_all()
    # meta.show_meta_details()

    # get_category('Flowers', 'Sativa')
    # get_category()
    # get_id()
    get_prerolls('Sativa')
