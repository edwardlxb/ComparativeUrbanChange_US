rural18 = WA_shp[WA_shp['Urban_2018'] == 'rural']
fig, ax = plt.subplots(1, figsize=(20,8))
ax = rural08.plot(column='Pop_Per_sqML_2008', ax=ax, linewidth=0.0, legend = True)
PlotFigure(ax, 14, "Rural Area in Washington State, 2008")

#map for rural 2018
rural18 = UrbanArea_2018[ UrbanArea_2018['Urban_2018'] == "rural" ].plot(
    column="Pop_Per_sqML_2018",
    linewidth=0.0,
    legend=True)
# remove the axis
rural18.axis("off")
rural18.set_title("Rural Area in 2018", fontdict={"fontsize": "15", "fontweight" : "2"})


#map for urban 2008
urban08 = UrbanArea_2018[ UrbanArea_2018['Urban_2018'] == "urban" ].plot(
    column="Pop_Per_sqML_2008",
    linewidth=0.0,
    legend=True)
# remove the axis
urban08.axis("off")
urban08.set_title("Urban Area in 2008", fontdict={"fontsize": "15", "fontweight" : "2"})


#map for urban 2018
urban18 = UrbanArea_2018[ UrbanArea_2018['Urban_2018'] == "urban" ].plot(
    column="Pop_Per_sqML_2018",
    linewidth=0.0,
    legend=True)
# remove the axis
urban18.axis("off")
urban18.set_title("Urban Area in 2018", fontdict={"fontsize": "15", "fontweight" : "2"})

