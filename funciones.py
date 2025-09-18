from gdeltdoc import GdeltDoc, Filters, near
import streamlit as st

gd = GdeltDoc()

def conteo_etnias(etnia, location, fecha_comienzo, fecha_fin):
    f = Filters(
    start_date = fecha_comienzo,
    end_date = fecha_fin,
    #keyword = etnia,
    #theme = "INDIGENOUS",
    near = near(10, etnia, "people"),
    #repeat = repeat(2, "protest"),
    )
    timevol = gd.timeline_search("timelinevolraw", f)

    return timevol

def articulos_fechas(etnia, fecha_comienzo, fecha_fin):
    f = Filters(
    start_date = fecha_comienzo,
    end_date = fecha_fin,
    num_records = 20,
    #keyword = "protest",
    #country = pais,
    #theme = "PROTEST",
    near = near(10, etnia, "people"),
    #repeat = repeat(2, "protest"),
    )
    articles = gd.article_search(f)

    return articles