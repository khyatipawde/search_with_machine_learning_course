For query classification:

How many unique categories did you see in your rolled up training data when you set the minimum number of queries per category to 1000? To 10000?
1000: 388
5000: 127
10000: 70

What were the best values you achieved for R@1, R@3, and R@5? You should have tried at least a few different models, varying the minimum number of queries per category, as well as trying different fastText parameters or query normalization. Report at least 2 of your runs.

**minimum_query: 1000, default**
N       10000
P@1     0.488
R@1     0.488

N       10000
P@2     0.299
R@2     0.598

N       10000
P@3     0.217
R@3     0.651

N       10000
P@5     0.143
R@5     0.713

**minimum_query: 1000, epoch: 25**
N       10000
P@1     0.537
R@1     0.537

N       10000
P@2     0.33
R@2     0.659

N       10000
P@3     0.239
R@3     0.717

**minimum_query: 10000, epoch: 25**
N       10000
P@1     0.593
R@1     0.593

N       10000
P@2     0.361
R@2     0.722

N       10000
P@3     0.261
R@3     0.783

**minimum_query: 10000, epoch: 25, test set: 30000**
N       30000
P@1     0.589
R@1     0.589

N       30000
P@2     0.359
R@2     0.719

N       30000
P@3     0.26
R@3     0.779

**minimum_query: 10000, epoch: 25, lr=0.5, wordNgram=2**
N       10000
P@1     0.587
R@1     0.587

N       10000
P@2     0.361
R@2     0.723

N       10000
P@3     0.263
R@3     0.79

N       10000
P@5     0.169
R@5     0.843

**minimum_query: 10000, epoch: 25, lr=0.5, wordNgram=2, training set: 100000**
N       10000
P@1     0.605
R@1     0.605

N       10000
P@2     0.37
R@2     0.74

N       10000
P@3     0.269
R@3     0.806

N       10000
P@5     0.172
R@5     0.862 ***BEST!***

For integrating query classification with search:

Give 2 or 3 examples of queries where you saw a dramatic positive change in the results because of filtering. Make sure to include the classifier output for those queries.

1) Category of a product

Query: dslr
Labels: ('__label__pcmcat180400050000', '__label__abcat0400000', '__label__abcat0401004', '__label__abcat0410010', '__label__abcat0101001'), Prob: [7.65266657e-01 1.61203355e-01 6.44741058e-02 5.51454304e-03
 3.55560071e-04]

WITH FILTERING: Despite the category being slightly incorrect 'DSLR Body & Lens', the results were all for DSLR cameras and not accessories - which feels more accurate.

Category: pcmcat180400050000, Prob: 0.7652666568756104, Sum: 0.7652666568756104

Selected Categories are:  ['pcmcat180400050000']

Name:  ['Canon - EOS Rebel T3i 18.0-Megapixel DSLR Camera with 18-55mm Lens - Black']
Categories:  ['Best Buy', 'Cameras & Camcorders', 'Digital Cameras', 'Digital SLR Cameras', 'DSLR Body & Lens']
Category IDs:  ['cat00000', 'abcat0400000', 'abcat0401000', 'abcat0401005', 'pcmcat180400050000']
Matching Category IDs:  ['pcmcat180400050000']
===================================================
Name:  ['Nikon - D5100 16.2-Megapixel DSLR Camera with 18-55mm VR Lens - Black']
Categories:  ['Best Buy', 'Cameras & Camcorders', 'Digital Cameras', 'Digital SLR Cameras', 'DSLR Body & Lens']
Category IDs:  ['cat00000', 'abcat0400000', 'abcat0401000', 'abcat0401005', 'pcmcat180400050000']
Matching Category IDs:  ['pcmcat180400050000']
===================================================
Name:  ['Canon - EOS Rebel T2i 18.0-Megapixel DSLR Camera with EF-S 18-55mm Lens - Black']
Categories:  ['Best Buy', 'Cameras & Camcorders', 'Digital Cameras', 'Digital SLR Cameras', 'DSLR Body & Lens']
Category IDs:  ['cat00000', 'abcat0400000', 'abcat0401000', 'abcat0401005', 'pcmcat180400050000']
Matching Category IDs:  ['pcmcat180400050000']
===================================================
Name:  ['Canon - EOS 60D 18.0-Megapixel DSLR Camera with 18-135mm Lens - Black']
Categories:  ['Best Buy', 'Cameras & Camcorders', 'Digital Cameras', 'Digital SLR Cameras', 'DSLR Body & Lens']
Category IDs:  ['cat00000', 'abcat0400000', 'abcat0401000', 'abcat0401005', 'pcmcat180400050000']
Matching Category IDs:  ['pcmcat180400050000']
===================================================
Name:  ['Nikon - D3200 24.2-Megapixel Digital SLR Camera with 18-55mm Zoom Lens - Black']
Categories:  ['Best Buy', 'Cameras & Camcorders', 'Digital Cameras', 'Digital SLR Cameras', 'DSLR Body & Lens']
Category IDs:  ['cat00000', 'abcat0400000', 'abcat0401000', 'abcat0401005', 'pcmcat180400050000']
Matching Category IDs:  ['pcmcat180400050000']
===================================================
Name:  ['PENTAX - Refurbished K2000 10.2-Megapixel DSLR Camera - White']
Categories:  ['Best Buy', 'Cameras & Camcorders', 'Digital Cameras', 'Digital SLR Cameras', 'DSLR Body & Lens']
Category IDs:  ['cat00000', 'abcat0400000', 'abcat0401000', 'abcat0401005', 'pcmcat180400050000']
Matching Category IDs:  ['pcmcat180400050000']
===================================================
Name:  ['PENTAX - Refurbished K-r 12.4-Megapixel DSLR Camera - Black']
Categories:  ['Best Buy', 'Cameras & Camcorders', 'Digital Cameras', 'Digital SLR Cameras', 'DSLR Body & Lens']
Category IDs:  ['cat00000', 'abcat0400000', 'abcat0401000', 'abcat0401005', 'pcmcat180400050000']
Matching Category IDs:  ['pcmcat180400050000']
===================================================
Name:  ['Sony - SLT-A35K 16.2-Megapixel DSLR Camera - Black']
Categories:  ['Best Buy', 'Cameras & Camcorders', 'Digital Cameras', 'Digital SLR Cameras', 'DSLR Body & Lens']
Category IDs:  ['cat00000', 'abcat0400000', 'abcat0401000', 'abcat0401005', 'pcmcat180400050000']
Matching Category IDs:  ['pcmcat180400050000']
===================================================
Name:  ['Nikon - 12.3-Megapixel D5000 DSLR Camera with 18-55mm Lens - Black']
Categories:  ['Best Buy', 'Cameras & Camcorders', 'Digital Cameras', 'Digital SLR Cameras', 'DSLR Body & Lens']
Category IDs:  ['cat00000', 'abcat0400000', 'abcat0401000', 'abcat0401005', 'pcmcat180400050000']
Matching Category IDs:  ['pcmcat180400050000']
===================================================
Name:  ['PENTAX - K-30 16.3-Megapixel DSLR Camera with 18-55mm Lens - White']
Categories:  ['Best Buy', 'Cameras & Camcorders', 'Digital Cameras', 'Digital SLR Cameras', 'DSLR Body & Lens']
Category IDs:  ['cat00000', 'abcat0400000', 'abcat0401000', 'abcat0401005', 'pcmcat180400050000']
Matching Category IDs:  ['pcmcat180400050000']

WITHOUT FILTERING: Without filtering, there were more accessories which showed up. ex: Travel Charger, Memory Card etc. 
===================================================

Name:  ['Canon - EOS Rebel T3i 18.0-Megapixel DSLR Camera with 18-55mm Lens - Black']
Categories:  ['Best Buy', 'Cameras & Camcorders', 'Digital Cameras', 'Digital SLR Cameras', 'DSLR Body & Lens']
Category IDs:  ['cat00000', 'abcat0400000', 'abcat0401000', 'abcat0401005', 'pcmcat180400050000']
Matching Category IDs:  []
===================================================
Name:  ['Nikon - D5100 16.2-Megapixel DSLR Camera with 18-55mm VR Lens - Black']
Categories:  ['Best Buy', 'Cameras & Camcorders', 'Digital Cameras', 'Digital SLR Cameras', 'DSLR Body & Lens']
Category IDs:  ['cat00000', 'abcat0400000', 'abcat0401000', 'abcat0401005', 'pcmcat180400050000']
Matching Category IDs:  []
===================================================
Name:  ['Canon - DSLR Gadget Bag - Black']
Categories:  ['Best Buy', 'Cameras & Camcorders', 'Camera & Camcorder Accessories', 'All Camera Accessories', 'Camera Bags & Cases']
Category IDs:  ['cat00000', 'abcat0400000', 'abcat0410000', 'abcat0410010', 'abcat0410001']
Matching Category IDs:  []
===================================================
Name:  ['DigiPower - Travel Charger']
Categories:  ['Best Buy', 'Cameras & Camcorders', 'Camera & Camcorder Accessories', 'DSLR Camera Accessories', 'DSLR Adapters & Chargers', 'DSLR Camera Chargers']
Category IDs:  ['cat00000', 'abcat0400000', 'abcat0410000', 'pcmcat241300050038', 'pcmcat240500050048', 'pcmcat240500050050']
Matching Category IDs:  []
===================================================
Name:  ['Canon - EOS Rebel T2i 18.0-Megapixel DSLR Camera with EF-S 18-55mm Lens - Black']
Categories:  ['Best Buy', 'Cameras & Camcorders', 'Digital Cameras', 'Digital SLR Cameras', 'DSLR Body & Lens']
Category IDs:  ['cat00000', 'abcat0400000', 'abcat0401000', 'abcat0401005', 'pcmcat180400050000']
Matching Category IDs:  []
===================================================
Name:  ['PNY - 16GB Secure Digital High Capacity (SDHC) Class 10 Memory Card']
Categories:  ['Best Buy', 'Cameras & Camcorders', 'Memory Cards & Readers', 'Memory Cards']
Category IDs:  ['cat00000', 'abcat0400000', 'abcat0404000', 'pcmcat225800050009']
Matching Category IDs:  []
===================================================
Name:  ['PNY - 8GB Secure Digital High Capacity (SDHC) Class 10 Memory Card']
Categories:  ['Best Buy', 'Cameras & Camcorders', 'Memory Cards & Readers', 'Memory Cards']
Category IDs:  ['cat00000', 'abcat0400000', 'abcat0404000', 'pcmcat225800050009']
Matching Category IDs:  []
===================================================
Name:  ['Nikon - D3100 14.2-Megapixel DSLR Camera with 18-55mm VR Lens - Red']
Categories:  ['Best Buy', 'Cameras & Camcorders', 'Digital Cameras', 'Digital SLR Cameras', 'All DSLRs']
Category IDs:  ['cat00000', 'abcat0400000', 'abcat0401000', 'abcat0401005', 'pcmcat186400050004']
Matching Category IDs:  []
===================================================
Name:  ['PNY - 32GB Secure Digital High Capacity (SDHC) Class 10 Memory Card']
Categories:  ['Best Buy', 'Cameras & Camcorders', 'Memory Cards & Readers', 'Memory Cards']
Category IDs:  ['cat00000', 'abcat0400000', 'abcat0404000', 'pcmcat225800050009']
Matching Category IDs:  []
===================================================
Name:  ['DigiPower - Travel Charger']
Categories:  ['Best Buy', 'Cameras & Camcorders', 'Camera & Camcorder Accessories', 'DSLR Camera Accessories', 'DSLR Adapters & Chargers', 'DSLR Camera Chargers']
Category IDs:  ['cat00000', 'abcat0400000', 'abcat0410000', 'pcmcat241300050038', 'pcmcat240500050048', 'pcmcat240500050050']
Matching Category IDs:  []
===================================================

2) Brand Specific Filtering

Query: apple
Normalized Query: appl

Labels: ('__label__pcmcat247400050001', '__label__abcat0201011', '__label__abcat0501000', '__label__pcmcat209000050007', '__label__pcmcat217900050000'), Prob: [0.39693868 0.06717022 0.05840404 0.0567083  0.04073555]


WITH FILTERING: correctly identified the top few categories of products sold by Apple (MacBooks, All iPod & MP3 Players, Desktop & All-in-One Computers) and returned those.

Category: pcmcat247400050001, Prob: 0.396938681602478, Sum: 0.396938681602478
Category: abcat0201011, Prob: 0.06717021763324738, Sum: 0.4641088992357254
Category: abcat0501000, Prob: 0.058404043316841125, Sum: 0.5225129425525665

Selected Categories are:  ['pcmcat247400050001', 'abcat0201011', 'abcat0501000']
ie. MacBooks, All iPod & MP3 Players, Desktop & All-in-One Computers

Name:  ['Apple® - iPod touch® 8GB* MP3 Player (4th Generation - Latest Model) - White']
Categories:  ['Best Buy', 'Audio & MP3', 'iPod & MP3 Players', 'All iPod & MP3 Players']
Category IDs:  ['cat00000', 'abcat0200000', 'abcat0201000', 'abcat0201011']
Matching Category IDs:  ['abcat0201011']
===================================================
Name:  ['Apple® - iPod touch® 8GB* MP3 Player (4th Generation - Latest Model) - Black']
Categories:  ['Best Buy', 'Audio & MP3', 'iPod & MP3 Players', 'All iPod & MP3 Players']
Category IDs:  ['cat00000', 'abcat0200000', 'abcat0201000', 'abcat0201011']
Matching Category IDs:  ['abcat0201011']
===================================================
Name:  ['Apple® - MacBook® Pro - 13.3" Display - 4GB Memory - 500GB Hard Drive']
Categories:  ['Best Buy', 'Computers & Tablets', 'Laptop & Netbook Computers', 'MacBooks']
Category IDs:  ['cat00000', 'abcat0500000', 'abcat0502000', 'pcmcat247400050001']
Matching Category IDs:  ['pcmcat247400050001']
===================================================
Name:  ['Apple® - iPod classic® 160GB* MP3 Player - Black']
Categories:  ['Best Buy', 'Audio & MP3', 'iPod & MP3 Players', 'All iPod & MP3 Players']
Category IDs:  ['cat00000', 'abcat0200000', 'abcat0201000', 'abcat0201011']
Matching Category IDs:  ['abcat0201011']
===================================================
Name:  ['Apple® - iPod touch® 32GB* MP3 Player (4th Generation - Latest Model) - Black']
Categories:  ['Best Buy', 'Audio & MP3', 'iPod & MP3 Players', 'All iPod & MP3 Players']
Category IDs:  ['cat00000', 'abcat0200000', 'abcat0201000', 'abcat0201011']
Matching Category IDs:  ['abcat0201011']
===================================================
Name:  ['Apple® - iPod touch® 32GB* MP3 Player (4th Generation - Latest Model) - White']
Categories:  ['Best Buy', 'Audio & MP3', 'iPod & MP3 Players', 'All iPod & MP3 Players']
Category IDs:  ['cat00000', 'abcat0200000', 'abcat0201000', 'abcat0201011']
Matching Category IDs:  ['abcat0201011']
===================================================
Name:  ['Apple® - 21.5" iMac® - 4GB Memory - 500GB Hard Drive']
Categories:  ['Best Buy', 'Computers & Tablets', 'Desktop & All-in-One Computers', 'Apple iMacs, Minis & Mac Pros']
Category IDs:  ['cat00000', 'abcat0500000', 'abcat0501000', 'pcmcat268200050003']
Matching Category IDs:  ['abcat0501000']
===================================================
Name:  ['Apple® - MacBook® Pro - 13.3" Display - 8GB Memory - 750GB Hard Drive']
Categories:  ['Best Buy', 'Computers & Tablets', 'Laptop & Netbook Computers', 'MacBooks']
Category IDs:  ['cat00000', 'abcat0500000', 'abcat0502000', 'pcmcat247400050001']
Matching Category IDs:  ['pcmcat247400050001']
===================================================
Name:  ['Apple® - MacBook Air® - 13.3" Display - 4GB Memory - 128GB Flash Storage']
Categories:  ['Best Buy', 'Computers & Tablets', 'Laptop & Netbook Computers', 'MacBooks']
Category IDs:  ['cat00000', 'abcat0500000', 'abcat0502000', 'pcmcat247400050001']
Matching Category IDs:  ['pcmcat247400050001']
===================================================
Name:  ['Apple® - iPod nano® 8GB* MP3 Player (6th Generation - Latest Model) - Blue']
Categories:  ['Best Buy', 'Audio & MP3', 'iPod & MP3 Players', 'All iPod & MP3 Players']
Category IDs:  ['cat00000', 'abcat0200000', 'abcat0201000', 'abcat0201011']
Matching Category IDs:  ['abcat0201011']
===================================================

WITHOUT FILTERING: Similar to the previous case, returns more accessories and less products

Name:  ['Apple® - Apple TV®']
Categories:  ['Best Buy', 'Computers & Tablets', 'Networking & Wireless', 'Home Entertainment Networking', 'Streaming Media Devices']
Category IDs:  ['cat00000', 'abcat0500000', 'abcat0503000', 'pcmcat161100050039', 'pcmcat161100050040']
Matching Category IDs:  []
===================================================
Name:  ['Apple® - Earbuds for Select Apple® iPod® Models']
Categories:  ['Best Buy', 'Audio & MP3', 'Headphones', 'All Headphones']
Category IDs:  ['cat00000', 'abcat0200000', 'abcat0204000', 'pcmcat144700050004']
Matching Category IDs:  []
===================================================
Name:  ['Apple - $15 iTunes Gift Card']
Categories:  ['Best Buy', 'Audio & MP3', 'iPod & MP3 Players', 'iTunes Gift Cards']
Category IDs:  ['cat00000', 'abcat0200000', 'abcat0201000', 'abcat0201007']
Matching Category IDs:  []
===================================================
Name:  ['Apple - $25 iTunes Gift Card']
Categories:  ['Best Buy', 'Audio & MP3', 'iPod & MP3 Players', 'iTunes Gift Cards']
Category IDs:  ['cat00000', 'abcat0200000', 'abcat0201000', 'abcat0201007']
Matching Category IDs:  []
===================================================
Name:  ['Apple® - USB Power Adapter for Apple® iPad™']
Categories:  ['Best Buy', 'Computers & Tablets', 'Tablets & iPad', 'iPad Accessories', 'iPad Cables, Chargers & Adapters']
Category IDs:  ['cat00000', 'abcat0500000', 'pcmcat209000050006', 'pcmcat217900050000', 'pcmcat218000050002']
Matching Category IDs:  []
===================================================
Name:  ['Zagg - InvisibleSHIELD HD for Apple® iPad® (3rd Generation)']
Categories:  ['Best Buy', 'Computers & Tablets', 'Tablets & iPad', 'iPad Accessories', 'iPad Screen Protection']
Category IDs:  ['cat00000', 'abcat0500000', 'pcmcat209000050006', 'pcmcat217900050000', 'pcmcat218000050003']
Matching Category IDs:  []
===================================================
Name:  ['Apple® - iPad® 2 with Wi-Fi - 16GB - Black']
Categories:  ['Best Buy', 'Computers & Tablets', 'Tablets & iPad', 'iPad']
Category IDs:  ['cat00000', 'abcat0500000', 'pcmcat209000050006', 'pcmcat209000050007']
Matching Category IDs:  []
===================================================
Name:  ['Apple® - iPad™ Digital Camera Connection Kit']
Categories:  ['Best Buy', 'Computers & Tablets', 'Tablets & iPad', 'iPad Accessories', 'iPad Cables, Chargers & Adapters']
Category IDs:  ['cat00000', 'abcat0500000', 'pcmcat209000050006', 'pcmcat217900050000', 'pcmcat218000050002']
Matching Category IDs:  []
===================================================
Name:  ['Apple® - Digital A/V Adapter']
Categories:  ['Best Buy', 'Computers & Tablets', 'Tablets & iPad', 'iPad Accessories', 'iPad Cables, Chargers & Adapters']
Category IDs:  ['cat00000', 'abcat0500000', 'pcmcat209000050006', 'pcmcat217900050000', 'pcmcat218000050002']
Matching Category IDs:  []
===================================================
Name:  ['ZAGG - InvisibleSHIELD HD for Apple® iPhone® 4 and 4S']
Categories:  ['Best Buy', 'Mobile Phones', 'Mobile Phone Accessories', 'Surface & Screen Protection', 'Screen Protectors']
Category IDs:  ['cat00000', 'abcat0800000', 'abcat0811002', 'pcmcat171900050031', 'pcmcat201900050009']
Matching Category IDs:  []
===================================================


Give 2 or 3 examples of queries where filtering hurt the results, either because the classifier was wrong or for some other reason. Again, include the classifier output for those queries.

1) Classified into a higher level, less popular category. 

Query: lion king
Normalized Query: lion king

Labels: ('__label__cat02015', '__label__cat02001', '__label__pcmcat247400050000', '__label__pcmcat209400050001', '__label__pcmcat174700050005'), Prob: [0.94073957 0.03562029 0.0054359  0.00434014 0.0035478 ]

WITH FILTERING: Did not return any results, should have returned relevant Lion King Games since we do sell those. 

Category: cat02015, Prob: 0.9407395720481873, Sum: 0.9407395720481873
Selected Categories are:  ['cat02015']

No results.

WITHOUT FILTERING: returns somewhat relevant results, which is a better experience than the no results case.

Name:  ["Disney's The Lion King Classic Game Collection - Windows"]
Categories:  ['Best Buy', 'Computers & Tablets', 'Software', "Children's Software"]
Category IDs:  ['cat00000', 'abcat0500000', 'abcat0508000', 'abcat0508035']
Matching Category IDs:  []
===================================================
Name:  ["Disney's The Lion King 1-1/2 - Game Boy Advance"]
Categories:  ['Best Buy', 'Video Games', 'Classic Video Game Systems', 'Game Boy Advance', 'Games', 'Kids & Family']
Category IDs:  ['cat00000', 'abcat0700000', 'pcmcat270900050006', 'abcat0708000', 'abcat0708002', 'abcat0708005']
Matching Category IDs:  []
===================================================
Name:  ["VTech - V.Smile Smartridge: Disney's The Lion King: Simba's Big Adventure"]
Categories:  ['Best Buy', 'Video Games', "Toys & Kids' Electronics", 'Learning Toys']
Category IDs:  ['cat00000', 'abcat0700000', 'abcat0714000', 'abcat0714011']
Matching Category IDs:  []
===================================================
Name:  ['Disney Friends - Nintendo DS']
Categories:  ['Best Buy', 'Video Games', 'Nintendo DS', 'Nintendo DS Games', 'Action & Adventure']
Category IDs:  ['cat00000', 'abcat0700000', 'abcat0707000', 'abcat0707002', 'abcat0707003']
Matching Category IDs:  []
===================================================
Name:  ['Disney Friends - Nintendo DS']
Categories:  ['Best Buy', 'Video Games', 'Nintendo DS', 'Nintendo DS Games', 'Kids & Family']
Category IDs:  ['cat00000', 'abcat0700000', 'abcat0707000', 'abcat0707002', 'abcat0707005']
Matching Category IDs:  []
===================================================
Name:  ["Disney's Collectors' Edition - PlayStation"]
Categories:  ['Best Buy', 'Video Games', 'Classic Video Game Systems', 'PlayStation 2', 'PS2 Games', 'Kids & Family']
Category IDs:  ['cat00000', 'abcat0700000', 'pcmcat270900050006', 'abcat0704000', 'abcat0704002', 'abcat0704006']
Matching Category IDs:  []
===================================================
Name:  ['Screenlife - Scene It?: Disney Magical Moments']
Categories:  ['Best Buy', 'Home', 'Toys & Games', 'Toys', 'Handheld Games']
Category IDs:  ['cat00000', 'pcmcat248700050021', 'pcmcat252700050006', 'pcmcat254300050001', 'abcat0714002']
Matching Category IDs:  []
===================================================
Name:  ["Disney's Extreme Skate Adventure - Game Boy Advance"]
Categories:  ['Best Buy', 'Video Games', 'Classic Video Game Systems', 'Game Boy Advance', 'Games', 'Kids & Family']
Category IDs:  ['cat00000', 'abcat0700000', 'pcmcat270900050006', 'abcat0708000', 'abcat0708002', 'abcat0708005']
Matching Category IDs:  []
===================================================
Name:  ["Disney's Extreme Skate Adventure - Nintendo GameCube"]
Categories:  ['Best Buy', 'Video Games', 'Classic Video Game Systems', 'GameCube', 'Games']
Category IDs:  ['cat00000', 'abcat0700000', 'pcmcat270900050006', 'abcat0709000', 'abcat0709002']
Matching Category IDs:  []
===================================================
Name:  ["Disney's Extreme Skate Adventure - PlayStation 2"]
Categories:  ['Best Buy', 'Video Games', 'Classic Video Game Systems', 'PlayStation 2', 'PS2 Games', 'Kids & Family']
Category IDs:  ['cat00000', 'abcat0700000', 'pcmcat270900050006', 'abcat0704000', 'abcat0704002', 'abcat0704006']
Matching Category IDs:  []
===================================================
2) Incorrect Classification for a broad query

Query: fantasy
Normalized Query: fantasi

Labels: ('__label__abcat0900000', '__label__cat02001', '__label__cat02015', '__label__abcat0515025', '__label__cat02009'), Prob: [0.38072291 0.25454837 0.07318293 0.06169258 0.03848162]


WITH FILTERING: Incorrectly classified as "coffee", returned only one inaccurate result

Category: abcat0900000, Prob: 0.38072291016578674, Sum: 0.38072291016578674
Category: cat02001, Prob: 0.2545483708381653, Sum: 0.635271281003952

Selected Categories are:  ['abcat0900000', 'cat02001']

Name:  ['Suchard - Hot Chocolate T-DISC for Braun Tassimo Hot Beverage Maker (8-Pack)']
Categories:  ['Best Buy', 'Appliances', 'Small Appliances', 'Coffee Makers & Espresso', 'Coffee Pods']
Category IDs:  ['cat00000', 'abcat0900000', 'abcat0912000', 'abcat0912005', 'abcat0912008']
Matching Category IDs:  ['abcat0900000']

WITHOUT FILTERING: resonable experience, returns the Final Fantasy Games first which could be what the user
originally intended. 

===================================================
Name:  ['Final Fantasy XII: Revenant Wings (Game Guide) - Nintendo DS']
Categories:  ['Best Buy', 'Video Games', 'Game Guides', 'Game Guides - Video Games']
Category IDs:  ['cat00000', 'abcat0700000', 'abcat0711000', 'abcat0711001']
Matching Category IDs:  []
===================================================
Name:  ['Final Fantasy XIII - 2 - Xbox 360']
Categories:  ['Best Buy', 'Video Games', 'Xbox 360', 'Xbox 360 Games']
Category IDs:  ['cat00000', 'abcat0700000', 'abcat0701000', 'abcat0701002']
Matching Category IDs:  []
===================================================
Name:  ['Game of Thrones - Xbox 360']
Categories:  ['Best Buy', 'Video Games', 'Xbox 360', 'Xbox 360 Games']
Category IDs:  ['cat00000', 'abcat0700000', 'abcat0701000', 'abcat0701002']
Matching Category IDs:  []
===================================================
Name:  ['Game of Thrones - PlayStation 3']
Categories:  ['Best Buy', 'Video Games', 'PlayStation 3', 'PS3 Games']
Category IDs:  ['cat00000', 'abcat0700000', 'abcat0703000', 'abcat0703002']
Matching Category IDs:  []
===================================================
Name:  ['Nintendo - Nintendo Wii Console (Red) with Wii Sports and New Super Mario Bros. Wii - Red']
Categories:  ['Best Buy', 'Video Games', 'Wii', 'Wii Consoles']
Category IDs:  ['cat00000', 'abcat0700000', 'abcat0706000', 'abcat0706001']
Matching Category IDs:  []
===================================================
Name:  ['Kingdoms of Amalur: Reckoning - Xbox 360']
Categories:  ['Best Buy', 'Video Games', 'Xbox 360', 'Xbox 360 Games']
Category IDs:  ['cat00000', 'abcat0700000', 'abcat0701000', 'abcat0701002']
Matching Category IDs:  []
===================================================
Name:  ['Warhammer 40,000: Space Marine - Xbox 360']
Categories:  ['Best Buy', 'Video Games', 'Xbox 360', 'Xbox 360 Games']
Category IDs:  ['cat00000', 'abcat0700000', 'abcat0701000', 'abcat0701002']
Matching Category IDs:  []
===================================================
Name:  ['Madden NFL 12 - Nintendo Wii']
Categories:  ['Best Buy', 'Video Games', 'Wii', 'Wii Games']
Category IDs:  ['cat00000', 'abcat0700000', 'abcat0706000', 'abcat0706002']
Matching Category IDs:  []
===================================================
Name:  ['Warhammer 40,000: Space Marine - PlayStation 3']
Categories:  ['Best Buy', 'Video Games', 'PlayStation 3', 'PS3 Games']
Category IDs:  ['cat00000', 'abcat0700000', 'abcat0703000', 'abcat0703002']
Matching Category IDs:  []
===================================================
