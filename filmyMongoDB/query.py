import pymongo
import time




myClient = pymongo.MongoClient("mongodb://localhost:27017/")
myDb = myClient["SBD4_Filmy"]

results_movies_ids = []

def srednia_ocena_rezysera_do_zeszlego_roku_mniejsza_od_4(collection_name_for_movies):
    pipeline = [
        {"$match": {
            "dataDodania": {"$gte": 2013, "$lte": 2015},
            "cena": {"$gte": 100, "$lte": 200},
            "dlugoscTrwania": {"$lte": 150},
            "rezyser.oceny.dataWystawienia": {"$lt": 2019},
        }},
        {"$project": {
            "name": "$nazwa",
            "idFilmu": "$idFilmu",
            "sredniaOcenaRezysera": {"$avg": "$rezyser.oceny.wartoscOceny"}
        }},
        {"$match": {"sredniaOcenaRezysera": {"$lt": 4}}}
    ]
    cur = myDb[collection_name_for_movies].aggregate(pipeline)
    local_results = set()
    for e in cur:
        local_results.add(e['idFilmu'])
        results_movies_ids.append(local_results)




# średnia wieku aktorów nie powinna przekraczać 40 lat w momencie wydania filmu
def srednia_wieku_aktorow_mniejsza_rowna_40_w_momencie_wydania_filmu(collection_name_for_movies):
    pipeline = [
        {"$project": {
            "name": "$nazwa",
            "idFilmu": "$idFilmu",
            "dataDodania": "$dataDodania",
            "sredniaDataUrodzeniaAktorow": {"$avg": "$aktorzy.dataUrodzenia"}
        }},
        {"$project": {
            "nazwa": "$name",
            "idFilmu": "$idFilmu",
            "sredniWiekAktorowWRokuWydaniaFilmu": {"$subtract": ["$dataDodania", "$sredniaDataUrodzeniaAktorow"]}
        }},
        {"$match": {"sredniWiekAktorowWRokuWydaniaFilmu": {"$lte": 40}}}
    ]
    cur = myDb[collection_name_for_movies].aggregate(pipeline)
    local_results = set()
    for e in cur:
        local_results.add(e['idFilmu'])
        results_movies_ids.append(local_results)





# Top 10 aktorów (bierzemy pod uwagę dane do zeszłego roku)
def top_10_aktorow(collection_name_for_actors):
    new_name_col = "top10_aktorow_" + collection_name_for_actors[8:12]
    pipeline = [
        {"$match": {"oceny.dataWystawienia": {"$lt": 2019}}},
        {"$project": {
            "idAktora": "$idAktora",
            "nazwisko": "$nazwisko",
            "sredniaOcena": {"$avg": "$oceny.wartoscOceny"}
        }},
        {"$sort": {"sredniaOcena": -1}},
        {"$limit": 10},
        # {"$out": new_name_col}
    ]
    cur = myDb[collection_name_for_actors].aggregate(pipeline)
    # for e in cur:

start = time.time()
srednia_ocena_rezysera_do_zeszlego_roku_mniejsza_od_4("filmy_100k")
srednia_wieku_aktorow_mniejsza_rowna_40_w_momencie_wydania_filmu("filmy_100k")
top_10_aktorow("aktorzy_100k")

# print(results_movies_ids[0].intersection(results_movies_ids[1]))
end = time.time()

elapsed = end - start
print(elapsed)