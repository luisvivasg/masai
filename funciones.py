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