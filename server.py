from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/files', methods=['GET'])
def get_files():
    files = [
     {"name": "Chemistry Notes Unit 1", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Chemistry"},

    {"name": "2020-21", "url": "https://abhi-42i.pages.dev/AI(2020-21).pdf", "category": "AI_pyq"},
    {"name": "2021-22", "url": "https://abhi-42i.pages.dev/AI(2021-22).pdf", "category": "AI_pyq"},
    {"name": "2015-16", "url": "https://abhi-42i.pages.dev/Chamistry1(2015-16).pdf", "category": "Chamistry_pyq"},
    {"name": "2015-16", "url": "https://abhi-42i.pages.dev/Chemistry(2015-16).pdf", "category": "Chemistry_pyq"},
    {"name": "2017-18", "url": "https://abhi-42i.pages.dev/Chemistry(2017-18)%20(2).pdf", "category": "Chemistry_pyq"},
    {"name": "2017-18", "url": "https://abhi-42i.pages.dev/Chemistry(2017-18).pdf", "category": "Chemistry_pyq"},
    {"name": "2018-19", "url": "https://abhi-42i.pages.dev/Chemistry(2018-19)%20(2).pdf", "category": "Chemistry_pyq"},
    {"name": "2018-19", "url": "https://abhi-42i.pages.dev/Chemistry(2018-19).pdf", "category": "Chemistry_pyq"},
    {"name": "2019-20", "url": "https://abhi-42i.pages.dev/Chemistry(2019-20).pdf", "category": "Chemistry_pyq"},
    {"name": "2020-21", "url": "https://abhi-42i.pages.dev/Chemistry(2020-21).pdf", "category": "Chemistry_pyq"},
    {"name": "2021-22", "url": "https://abhi-42i.pages.dev/Chemistry(2021-22).pdf", "category": "Chemistry_pyq"},
    {"name": "2022-23", "url": "https://abhi-42i.pages.dev/Chemistry(2022-23).pdf", "category": "Chemistry_pyq"},
    {"name": "2023-24", "url": "https://abhi-42i.pages.dev/Chemistry(2023-24).pdf", "category": "Chemistry_pyq"},
    {"name": "2021-22", "url": "https://abhi-42i.pages.dev/Chemistry1(2021-22).pdf", "category": "Chemistry_pyq"},
    {"name": "2015-16", "url": "https://abhi-42i.pages.dev/Electrical(2015-16).pdf", "category": "Electrical_pyq"},
    {"name": "2017-18", "url": "https://abhi-42i.pages.dev/Electrical(2017-18)%20(2).pdf", "category": "Electrical_pyq"},
    {"name": "2017-18", "url": "https://abhi-42i.pages.dev/Electrical(2017-18).pdf", "category": "Electrical_pyq"},
    {"name": "2018-19", "url": "https://abhi-42i.pages.dev/Electrical(2018-19)%20(2).pdf", "category": "Electrical_pyq"},
    {"name": "2018-19", "url": "https://abhi-42i.pages.dev/Electrical(2018-19).pdf", "category": "Electrical_pyq"},
    {"name": "2019-20", "url": "https://abhi-42i.pages.dev/Electrical(2019-20).pdf", "category": "Electrical_pyq"},
    {"name": "2020-21", "url": "https://abhi-42i.pages.dev/Electrical(2020-21).pdf", "category": "Electrical_pyq"},
    {"name": "2021-22", "url": "https://abhi-42i.pages.dev/Electrical(2021-22).pdf", "category": "Electrical_pyq"},
    {"name": "2022-23", "url": "https://abhi-42i.pages.dev/Electrical(2022-23).pdf", "category": "Electrical_pyq"},
    {"name": "2023-24", "url": "https://abhi-42i.pages.dev/Electrical(2023-24).pdf", "category": "Electrical_pyq"},
    {"name": "2021-22", "url": "https://abhi-42i.pages.dev/Electrical1(2021-22).pdf", "category": "Electrical_pyq"},
    {"name": "2015-16", "url": "https://abhi-42i.pages.dev/Electronics(2015-16).pdf", "category": "Electronics_pyq"},
    {"name": "2017-18", "url": "https://abhi-42i.pages.dev/Electronics(2017-18)%20(2).pdf", "category": "Electronics_pyq"},
    {"name": "2017-18", "url": "https://abhi-42i.pages.dev/Electronics(2017-18).pdf", "category": "Electronics_pyq"},
    {"name": "2020-21", "url": "https://abhi-42i.pages.dev/Electronics(2020-21).pdf", "category": "Electronics_pyq"},
    {"name": "2022-23", "url": "https://abhi-42i.pages.dev/Electronics(2022-23).pdf", "category": "Electronics_pyq"},
    {"name": "2023-24", "url": "https://abhi-42i.pages.dev/Electronics(2023-24).pdf", "category": "Electronics_pyq"},
    {"name": "2015-16", "url": "https://abhi-42i.pages.dev/Electronics1(2015-16).pdf", "category": "Electronics_pyq"}
    
    {"name": "2020-21", "url": "https://abhi-42i.pages.dev/EmergingDomain(2021-22).pdf", "category": "EmergingDomain_pyq"},
    {"name": "2020-21", "url": "https://abhi-42i.pages.dev/Emergingtechnology(2020-21).pdf", "category": "Emergingtechnology_pyq"},
    {"name": "2021-22", "url": "https://abhi-42i.pages.dev/Emergingtechnology(2021-22).pdf", "category": "Emergingtechnology_pyq"},
    {"name": "2015-16", "url": "https://abhi-42i.pages.dev/Evs(2015-16).pdf", "category": "Evs_pyq"},
    {"name": "2022-23", "url": "https://abhi-42i.pages.dev/Evs(2022-23).pdf", "category": "Evs_pyq"},
    {"name": "2023-24", "url": "https://abhi-42i.pages.dev/Evs(2023-24).pdf", "category": "Evs_pyq"},
    {"name": "2015-16", "url": "https://abhi-42i.pages.dev/Evs1(2015-16).pdf", "category": "Evs_pyq"},
    {"name": "2022-23", "url": "https://abhi-42i.pages.dev/HumanValue(2022-23).pdf", "category": "HumanValue_pyq"},
    {"name": "2015-16", "url": "https://abhi-42i.pages.dev/Machanical2(2015-16).pdf", "category": "Machanical_pyq"},
    {"name": "2015-16", "url": "https://abhi-42i.pages.dev/ManufactuaringPractices(2015-16).pdf", "category": "ManufactuaringPractices_pyq"},
    {"name": "2015-16", "url": "https://abhi-42i.pages.dev/ManufactuaringProcess1(2015-16).pdf", "category": "ManufactuaringProcess_pyq"},
    {"name": "2017-18", "url": "https://abhi-42i.pages.dev/Maths1(2017-18).pdf", "category": "Maths1_pyq"},
    {"name": "2018-19", "url": "https://abhi-42i.pages.dev/Maths1(2018-19).pdf", "category": "Maths1_pyq"},
    {"name": "2019-20", "url": "https://abhi-42i.pages.dev/Maths1(2019-20).pdf", "category": "Maths1_pyq"},
    {"name": "2020-21", "url": "https://abhi-42i.pages.dev/Maths1(2020-21).pdf", "category": "Maths1_pyq"},
    {"name": "2021-22", "url": "https://abhi-42i.pages.dev/Maths1(2021-22).pdf", "category": "Maths1_pyq"},
    {"name": "2022-23", "url": "https://abhi-42i.pages.dev/Maths1(2022-23).pdf", "category": "Maths1_pyq"},
    {"name": "2023-24", "url": "https://abhi-42i.pages.dev/Maths1(2023-24).pdf", "category": "Maths1_pyq"},
    {"name": "2015-16", "url": "https://abhi-42i.pages.dev/Maths2(2015-16).pdf", "category": "Maths2_pyq"},
    {"name": "2017-18", "url": "https://abhi-42i.pages.dev/Maths2(2017-18).pdf", "category": "Maths2_pyq"},
    {"name": "2018-19", "url": "https://abhi-42i.pages.dev/Maths2(2018-19).pdf", "category": "Maths2_pyq"},
    {"name": "2021-22", "url": "https://abhi-42i.pages.dev/Maths2(2021-22).pdf", "category": "Maths2_pyq"},
    {"name": "2022-23", "url": "https://abhi-42i.pages.dev/Maths2(2022-23).pdf", "category": "Maths2_pyq"},
    {"name": "2023-24", "url": "https://abhi-42i.pages.dev/Maths2(2023-24).pdf", "category": "Maths2_pyq"},
    {"name": "2015-16", "url": "https://abhi-42i.pages.dev/Maths2.1(2015-16).pdf", "category": "Maths2_pyq"},
    {"name": "2015-16", "url": "https://abhi-42i.pages.dev/Mechanical(2015-16).pdf", "category": "Mechanical_pyq"},
    {"name": "2017-18", "url": "https://abhi-42i.pages.dev/Mechanical(2017-18)%20(2).pdf", "category": "Mechanical_pyq"},
    {"name": "2017-18", "url": "https://abhi-42i.pages.dev/Mechanical(2017-18).pdf", "category": "Mechanical_pyq"},
    {"name": "2020-21", "url": "https://abhi-42i.pages.dev/Mechanical(2020-21).pdf", "category": "Mechanical_pyq"},
    {"name": "2021-22", "url": "https://abhi-42i.pages.dev/Mechanical(2021-22).pdf", "category": "Mechanical_pyq"},
    {"name": "2022-23", "url": "https://abhi-42i.pages.dev/Mechanical(2022-23).pdf", "category": "Mechanical_pyq"},
    {"name": "2023-24", "url": "https://abhi-42i.pages.dev/Mechanical(2023-24).pdf", "category": "Mechanical_pyq"},
    {"name": "2015-16", "url": "https://abhi-42i.pages.dev/Mechanical1(2015-16).pdf", "category": "Mechanical_pyq"},
    {"name": "2023-24", "url": "https://abhi-42i.pages.dev/Mechanical2023-24.pdf", "category": "Mechanical_pyq"},
    {"name": "2015-16", "url": "https://abhi-42i.pages.dev/Physics(2015-16).pdf", "category": "Physics_pyq"},
    {"name": "2017-18", "url": "https://abhi-42i.pages.dev/Physics(2017-18)%20(2).pdf", "category": "Physics_pyq"},
    {"name": "2017-18", "url": "https://abhi-42i.pages.dev/Physics(2017-18).pdf", "category": "Physics_pyq"},
    {"name": "2018-19", "url": "https://abhi-42i.pages.dev/Physics(2018-19)%20(2).pdf", "category": "Physics_pyq"},
    {"name": "2018-19", "url": "https://abhi-42i.pages.dev/Physics(2018-19).pdf", "category": "Physics_pyq"},
    {"name": "2019-20", "url": "https://abhi-42i.pages.dev/Physics(2019-20).pdf", "category": "Physics_pyq"},
    {"name": "2020-21", "url": "https://abhi-42i.pages.dev/Physics(2020-21).pdf", "category": "Physics_pyq"},
    {"name": "2021-22", "url": "https://abhi-42i.pages.dev/Physics(2021-22).pdf", "category": "Physics_pyq"},
    {"name": "2022-23", "url": "https://abhi-42i.pages.dev/Physics(2022-23).pdf", "category": "Physics_pyq"},
    {"name": "2023-24", "url": "https://abhi-42i.pages.dev/Physics(2023-24).pdf", "category": "Physics_pyq"}
]


    return jsonify(files)


import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  
    app.run(host='0.0.0.0', port=port)



