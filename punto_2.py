from lifestore_file import lifestore_sales, lifestore_products

# El proposito es encontrar toda la info para cada categoria

# Hacer el analisis de reviews por categoria tambien la de ventas.
prod_reviews = {}
for sale in lifestore_sales:
    # prod y review de venta
    prod_id = sale[1]
    review = sale[2]
    # categorizar por id
    if prod_id not in prod_reviews.keys():
        prod_reviews[prod_id] = []
    prod_reviews[prod_id].append(review)

# print(prod_reviews)

id_rev_prom = {}
for id, reviews in prod_reviews.items():
    # print(id, reviews)
    rev_prom = sum(reviews) / len(reviews)
    rev_prom = int(rev_prom*100)/100
    id_rev_prom[id] = [rev_prom, len(reviews)]

# Para ordenar siempre es mas facil usar listas.
dicc_en_list = []
for id, lista in id_rev_prom.items():
    # print(id, rev_prom)
    rev_prom = lista[0]
    cant = lista[1]
    sub = [id, rev_prom, cant]
    dicc_en_list.append(sub)


def seg_elemnto(sub):
    return sub[1]

dicc_en_list = sorted(dicc_en_list, key=seg_elemnto, reverse=True)
# dicc_en_list = sorted(dicc_en_list, key=lambda lista:lista[2], reverse=True)

for sublista in dicc_en_list:
    print(sublista)

for sublista in dicc_en_list[-5:]:
    id, rev, num = sublista
    indice_lsp = id - 1
    prod = lifestore_products[indice_lsp]
    nombre = prod[1]
    nombre = nombre.split(' ')
    nombre = ' '.join(nombre[:4])
    print(f'El producto "{nombre}":\n\trev_prom: {rev}, num de ventas: {num}')
# category_ids = {}
# for prod in lifestore_products:
#     prod_id = prod[0]
#     category = prod[3]
#     if category not in category_ids.keys():
#         category_ids[category] = []
#     category_ids[category].append(prod_id)

# print(category_ids)

# resultados_por_categoria = {}
# for category, prod_id_list in category_ids.items():
#     reviews = []
#     ganancias = 0
#     ventas = 0
#     for prod_id in prod_id_list:
#         if prod_id not in prod_reviews.keys():
#             continue
#         reviews_ventas = prod_reviews[prod_id]
#         precio = lifestore_products[prod_id][2]
#         total_sales = len(reviews_ventas)
#         g = precio * total_sales
#         reviews += reviews_ventas
#         ganancias += g
#         ventas += total_sales

#     prom_reviews = sum(reviews) / len(reviews)

#     resultados_por_categoria[category] = {
#         'review_promedio': prom_reviews,
#         'ganancias': ganancias,
#         'ventas_totales': ventas
#     }


#  cat -> id -> reviews -> la cantidad de reviews es la cantidad de ventas
