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






        {"name": "Chemistry Notes Chapter 2", "url": "https://raw.githubusercontent.com/username/repository/branch/path/to/chapter2.pdf", "category": "Chemistry"},
        {"name": "Physics Notes Chapter 1", "url": "https://raw.githubusercontent.com/username/repository/branch/path/to/chapter1.pdf", "category": "Electrical_pyq"},
        {"name": "Physics Notes Chapter 2", "url": "https://raw.githubusercontent.com/username/repository/branch/path/to/chapter2.pdf", "category": "Electrical_notes"},
        {"name": "Chemistry Notes Chapter 3", "url": "https://raw.githubusercontent.com/username/repository/branch/path/to/chapter3.pdf", "category": "Chemistry_pyq"},
        {"name": "Physics Notes Chapter 3", "url": "https://raw.githubusercontent.com/username/repository/branch/path/to/chapter3.pdf", "category": "Physics_notes"}
    ]
    return jsonify(files)


import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  
    app.run(host='0.0.0.0', port=port)



