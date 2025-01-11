from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/files', methods=['GET'])
def get_files():
    files = [
        {"name": "Chemistry Notes Unit 1", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Chemistry"},
        {"name": "Chemistry Notes Unit 2", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Chemistry"},
        {"name": "Chemistry Notes Unit 3", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Chemistry"},
        {"name": "Chemistry Notes Unit 4", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Chemistry"},
        {"name": "Chemistry Notes Unit 5", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Chemistry"},

    
        {"name": "Chemistry  Unit 1", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Chemistry_pyq"},
        {"name": "Chemistry  Unit 2", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Chemistry_pyq"},
        {"name": "Chemistry  Unit 3", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Chemistry_pyq"},
        {"name": "Chemistry  Unit 4", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Chemistry_pyq"},
        {"name": "Chemistry  Unit 5", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Chemistry_pyq"},

        
        {"name": "Physics Unit 1", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Physics_notes"},
        {"name": "Physics Unit 2", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Physics_notes"},
        {"name": "Physics Unit 3", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Physics_notes"},
        {"name": "Physics Unit 4", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Physics_notes"},
        {"name": "Physics Unit 5", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Physics_notes"},

    
        {"name": "Physics Unit 1", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Physics_pyq"},
        {"name": "Physics Unit 2", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Physics_pyq"},
        {"name": "Physics Unit 3", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Physics_pyq"},
        {"name": "Physics Unit 4", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Physics_pyq"},
        {"name": "Physics Unit 5", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Physics_pyq"},


        
    {"name": "Maths1 Unit 1", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Maths1_notes"},
    {"name": "Maths1 Unit 2", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Maths1_notes"},
    {"name": "Maths1 Unit 3", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Maths1_notes"},
    {"name": "Maths1 Unit 4", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Maths1_notes"},
    {"name": "Maths1 Unit 5", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Maths1_notes"},

    {"name": "Maths1 Unit 1", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Maths1_pyq"},
    {"name": "Maths1 Unit 2", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Maths1_pyq"},
    {"name": "Maths1 Unit 3", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Maths1_pyq"},
    {"name": "Maths1 Unit 4", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Maths1_pyq"},
    {"name": "Maths1 Unit 5", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Maths1_pyq"},

    {"name": "Electrical Unit 1", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Electrical_notes"},
    {"name": "Electrical Unit 2", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Electrical_notes"},
    {"name": "Electrical Unit 3", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Electrical_notes"},
    {"name": "Electrical Unit 4", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Electrical_notes"},
    {"name": "Electrical Unit 5", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Electrical_notes"},

    {"name": "Electrical Unit 1", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Electrical_pyq"},
    {"name": "Electrical Unit 2", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Electrical_pyq"},
    {"name": "Electrical Unit 3", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Electrical_pyq"},
    {"name": "Electrical Unit 4", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Electrical_pyq"},
    {"name": "Electrical Unit 5", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Electrical_pyq"},

    {"name": "Electronics Unit 1", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Electronics_notes"},
    {"name": "Electronics Unit 2", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Electronics_notes"},
    {"name": "Electronics Unit 3", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Electronics_notes"},
    {"name": "Electronics Unit 4", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Electronics_notes"},
    {"name": "Electronics Unit 5", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Electronics_notes"},

    {"name": "Electronics Unit 1", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Electronics_pyq"},
    {"name": "Electronics Unit 2", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Electronics_pyq"},
    {"name": "Electronics Unit 3", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Electronics_pyq"},
    {"name": "Electronics Unit 4", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Electronics_pyq"},
    {"name": "Electronics Unit 5", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Electronics_pyq"},

    {"name": "Pps Unit 1", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Pps_notes"},
    {"name": "Pps Unit 2", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Pps_notes"},
    {"name": "Pps Unit 3", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Pps_notes"},
    {"name": "Pps Unit 4", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Pps_notes"},
    {"name": "Pps Unit 5", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Pps_notes"},

    {"name": "Pps Unit 1", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Pps_pyq"},
    {"name": "Pps Unit 2", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Pps_pyq"},
    {"name": "Pps Unit 3", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Pps_pyq"},
    {"name": "Pps Unit 4", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Pps_pyq"},
    {"name": "Pps Unit 5", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Pps_pyq"},

    {"name": "Mechanical Unit 1", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Mechanical_notes"},
    {"name": "Mechanical Unit 2", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Mechanical_notes"},
    {"name": "Mechanical Unit 3", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Mechanical_notes"},
    {"name": "Mechanical Unit 4", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Mechanical_notes"},
    {"name": "Mechanical Unit 5", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Mechanical_notes"},

    {"name": "Mechanical Unit 1", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Mechanical_pyq"},
    {"name": "Mechanical Unit 2", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Mechanical_pyq"},
    {"name": "Mechanical Unit 3", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Mechanical_pyq"},
    {"name": "Mechanical Unit 4", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Mechanical_pyq"},
    {"name": "Mechanical Unit 5", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Mechanical_pyq"},

    {"name": "Evs Unit 1", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Evs_notes"},
    {"name": "Evs Unit 2", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Evs_notes"},
    {"name": "Evs Unit 3", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Evs_notes"},
    {"name": "Evs Unit 4", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Evs_notes"},
    {"name": "Evs Unit 5", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Evs_notes"},

    {"name": "Evs Unit 1", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Evs_pyq"},
    {"name": "Evs Unit 2", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Evs_pyq"},
    {"name": "Evs Unit 3", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Evs_pyq"},
    {"name": "Evs Unit 4", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Evs_pyq"},
    {"name": "Evs Unit 5", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Evs_pyq"},

    {"name": "Softskill Unit 1", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Softskill_notes"},
    {"name": "Softskill Unit 2", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Softskill_notes"},
    {"name": "Softskill Unit 3", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Softskill_notes"},
    {"name": "Softskill Unit 4", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Softskill_notes"},
    {"name": "Softskill Unit 5", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Softskill_notes"},

    {"name": "Softskill Unit 1", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Softskill_pyq"},
    {"name": "Softskill Unit 2", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Softskill_pyq"},
    {"name": "Softskill Unit 3", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Softskill_pyq"},
    {"name": "Softskill Unit 4", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Softskill_pyq"},
    {"name": "Softskill Unit 5", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Softskill_pyq"},

    {"name": "Maths2 Unit 1", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Maths2_notes"},
    {"name": "Maths2 Unit 2", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Maths2_notes"},
    {"name": "Maths2 Unit 3", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Maths2_notes"},
    {"name": "Maths2 Unit 4", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Maths2_notes"},
    {"name": "Maths2 Unit 5", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Maths2_notes"},

    {"name": "Maths2 Unit 1", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Maths2_pyq"},
    {"name": "Maths2 Unit 2", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Maths2_pyq"},
    {"name": "Maths2 Unit 3", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Maths2_pyq"},
    {"name": "Maths2 Unit 4", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Maths2_pyq"},
    {"name": "Maths2 Unit 5", "url": "https://abhi-42i.pages.dev/B.Tech_2nd_Yr_CSE_v3.pdf", "category": "Maths2_pyq"}
]





        
    
    return jsonify(files)


import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  
    app.run(host='0.0.0.0', port=port)



