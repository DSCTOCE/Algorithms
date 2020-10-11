from covid import  Covid
import matplotlib.pyplot as pyplot


country=input("Enter your country name: ")
covid=Covid()
data=covid.get_status_by_country_name(country)
ment={
    key: data[key]
    for key in data.keys() & {"confirmed", "active", "deaths", "recovered"}
}

n=list(ment.keys())
v=list(ment.values())
print(ment)



pyplot.title(country)
pyplot.bar(range(len(ment)), v, tick_label=n)
pyplot.show()