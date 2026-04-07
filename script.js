const spec = {
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "autosize": { "type": "fit", "contains": "padding" },
  "padding": { "left": 20, "top": 20, "right": 30, "bottom": 20 },
  
  "title": {
    "text": "全球人均温室气体排放量历史趋势",
    "subtitle": { "signal": "'当前选中年份: ' + year_selection + ' | 点击地图国家查看历史趋势'" },
    "fontSize": 22, "anchor": "start", "color": "#1f2937", "offset": 20
  },
  
  "background": "#ffffff",
  
  "data": {
    "url": "data/data_processed.csv",
    "format": { "type": "csv", "parse": { "id": "number", "year": "number", "co2_per_capita": "number" } }
  },

  "params": [
    {
      "name": "year_selection",
      "value": 2022,
      "bind": { "input": "range", "min": 1990, "max": 2024, "step": 1, "name": "时间轴: " }
    }
  ],

  "vconcat": [
    {
      // --- 地图部分 ---
      "width": 800, 
      "height": 400,
      "projection": { "type": "equalEarth" },
      "layer": [
        {
          "data": {
            "url": "data/countries-50m.json",
            "format": { "type": "topojson", "feature": "countries" }
          },
          "mark": { "type": "geoshape", "fill": "#f3f4f6", "stroke": "#ffffff", "strokeWidth": 0.5 }
        },
        {
          "params": [
            { "name": "click_country", "select": { "type": "point", "fields": ["country"], "on": "click" } }
          ],
          "transform": [
            { "filter": "datum.year == year_selection" },
            {
              "lookup": "id",
              "from": {
                "data": { "url": "data/countries-50m.json", "format": { "type": "topojson", "feature": "countries" } },
                "key": "id"
              },
              "as": "geo_shape"
            }
          ],
          "mark": { "type": "geoshape", "stroke": "#ffffff" },
          "encoding": {
            "shape": { "field": "geo_shape", "type": "geojson" },
            "color": {
              "field": "co2_per_capita",
              "type": "quantitative",
              "scale": { "scheme": "oranges", "domain": [0, 20] },
              "legend": { "title": "吨/人", "orient": "right", "gradientLength": 200 }
            },
            "opacity": {
              "condition": { "param": "click_country", "value": 1 },
              "value": 0.3
            },
            "tooltip": [
              { "field": "country", "type": "nominal", "title": "国家" },
              { "field": "co2_per_capita", "type": "quantitative", "title": "排放量", "format": ".2f" }
            ]
          }
        }
      ]
    },  
    {
      // --- 折线图部分 ---
      "width": 800,
      "height": 150,
      "transform": [{ "filter": { "param": "click_country", "empty": false } }],
      "layer": [
        {
          "mark": { 
            "type": "area", 
            "line": { "color": "#f97316" }, 
            "color": { "gradient": "linear", "stops": [{ "offset": 0, "color": "white" }, { "offset": 1, "color": "#f97316" }], "x1": 1, "y1": 1, "x2": 1, "y2": 0 }, 
            "opacity": 0.2, 
            "interpolate": "monotone" 
          },
          "encoding": {
            "x": { 
              "field": "year", 
              "type": "quantitative", 
              "axis": { "format": "d", "labelFlush": true, "grid": false }, 
              "title": "年份",
              "scale": { "domain": [1989, 2023] }
            },
            "y": { 
              "field": "co2_per_capita", 
              "type": "quantitative", 
              "title": "人均排放(吨/人)",
              "axis": { "gridDash": [2, 2], "titlePadding": 10 }
            }
          }
        },
        {
          "mark": { "type": "rule", "color": "#374151", "strokeDash": [4, 4] },
          "encoding": { "x": { "datum": { "expr": "year_selection" }, "type": "quantitative" } }
        }
      ],
      "title": {
        "text": { "signal": "click_country.country ? '历史趋势: ' + click_country.country : ''" },
        "fontSize": 16, "anchor": "start", "offset": 10
      }
    }
  ],
  "config": {
    "view": { "stroke": "transparent" }
  }
};

vegaEmbed('#vis', spec, { "actions": false });