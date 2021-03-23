cd ..
cd venv
cd scripts
call activate.bat
cd ..
cd ..
cd Artyvis
scrapy crawl --nolog houseofindya -o necklaces.json 
scrapy crawl --nolog houseofindya -o necklaces.csv