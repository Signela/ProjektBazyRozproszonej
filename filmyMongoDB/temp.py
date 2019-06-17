
# przynajmniej 1 z Top 10 aktorów grał w tym filmie (bierzemy pod uwagę dane do zeszłego roku)
def przynajmniej_jeden_z_top_10_aktorow_gral_w_filmie(collection_name_for_actors, collection_name_for_movies):
    top_10_actors_col_name = "top10_aktorow_" + collection_name_for_movies[8:12]
    # pipeline = [
    #     {"$facet": {
    #         "c1": [
    #             {"$project": {
    #                 "nazwa": "$nazwa",
    #                 "aktorzy": "$aktorzy",
    #                 # "aktorzy.idAktora": {"$in": ""}
    #             },
    #             "as": "col1"
    #             },
    #         ],
    #
    #         "c2": [
    #             {"$lookup": {
    #                 "from": top_10_actors_col_name,
    #             },
    #                 {"$unwind": "$emails"},
    #                 {"$group": {"_id": null, emails: {$push: "$emails.address"}}},
    #                 {"$project": {emails: true, _id: false}}
    #             "as": "col2"
    #             },
    #         ]
    #     }}
    # ]
    cur = myDb[collection_name_for_movies].aggregate(pipeline)
    for e in cur:
        print(e)

# przynajmniej_jeden_z_top_10_aktorow_gral_w_filmie("aktorzy_100k", "filmy_100k")


# średnia ocen filmu w roku ich wydania była >2.5
# i, które w zeszłym roku miały średnią > 2,
# jednakże oceny które bierzemy pod uwagę musiały zostać wystawione przez użytkowników pomiędzy 20 a 30 rokiem życia w momencie wystawienia oceny
def srednie_oceny_z_wymaganiami(collection_name_for_movies):
    pipeline = [
        # {"$match": {"$oceny.dataWystawienia": {"$eq": "$dataDodania"}}},
        {"$project": {
            "name": "$nazwa",
            "idFilmu": "$idFilmu",
            # "sredniaOcenaFilmu": {"$avg": {"$oceny.wartoscOceny"}},
        }},
        # {"$match": { "o": {"$gt": 2.5}}}
    ]
    cur = myDb[collection_name_for_movies].aggregate(pipeline)
    for e in cur:
        print(e)
        # {"$project": {
        #     "name": "$nazwa",
        #     "dataDodania": "$dataDodania",
        #     "sredniaOcenaFilmu": {"$avg": "$oceny.wartoscOceny"}
        # }},
        # {"$project": {
        #     "nazwa": "$name",
        #     "sredniWiekAktorowWRokuWydaniaFilmu": {"$subtract": ["$dataDodania", "$sredniaDataUrodzeniaAktorow"]}
        # }},
        # {"$match": {"sredniWiekAktorowWRokuWydaniaFilmu": {"$lte": 40}}}

# def srednie_oceny_z_wymaganiami(collection_name_for_movies):
#     pipeline = [
#         {"$project": {
#             "name": "$nazwa",
#             "id": "$idFilmu",
#             "sredniaOcenaFilmu": {"$avg": "$oceny.wartoscOceny"},
#         }},
#     ]
#     cur = myDb[collection_name_for_movies].aggregate(pipeline)
#     for e in cur:
#         print(e)

# srednie_oceny_z_wymaganiami("filmy_100k")
#