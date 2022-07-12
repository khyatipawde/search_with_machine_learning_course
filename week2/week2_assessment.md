
## LEVEL 1: For deriving synonyms from content ##
1. What precision (P@1) were you able to achieve?
N       10000
P@1     **0.967**
R@1     0.967

2. What fastText parameters did you use?
`-lr 1.0, -epoch 25`
Commands: `~/fastText-0.9.2/fasttext supervised -input /workspace/datasets/fasttext/pruned_training_data.txt -output /workspace/datasets/fasttext/pruned_product_classifier  -lr 1.0 -epoch 25`
`~/fastText-0.9.2/fasttext test /workspace/datasets/fasttext/pruned_product_classifier.bin  /workspace/datasets/fasttext/pruned_test_data.txt`

3. How did you transform the product names?
Lowercased, removed non-alphanumeric chars except _ and removed extra spaces.

4. How did you prune infrequent category labels, and how did that affect your precision?
Pruned infrequent (which had <500 categories) labels using a pandas script. Helped with precision, resulted in a massive increase: from 0.623 to 0.967.

5. How did you prune the category tree, and how did that affect your precision?
I didn't get there.

## LEVEL 2: For deriving synonyms from content ##

1. What were the results for your best model in the tokens used for evaluation?

Query word? headphones
headphone 0.924937
earbud 0.908463
ear 0.857572
earphones 0.807543
bud 0.783763
earbuds 0.758269
2xl 0.732515
hesh 0.728457
yurbuds 0.713169
gumy 0.70957

Query word? laptop
laptops 0.742242
laps 0.708303
176 0.698773
durabook 0.692894
s5919 0.692485
ultrabook 0.688238
156b 0.6859
172 0.683434
lapgear 0.682708
lap 0.678622

Query word? freezer
freezers 0.92098
refrigerator 0.80411
refrigerators 0.772334
frost 0.754727
side 0.748935
mug 0.729545
cu 0.713289
bottom 0.711814
satina 0.701586
monochromatic 0.695408

Query word? nintendo
nintendogs 0.979258
ds 0.886968
wii 0.885358
3ds 0.812321
gamecube 0.807711
zhu 0.743679
mysims 0.727757
zhuzhu 0.724732
zelda 0.719905
psp 0.719257

Query word? whirlpool
whirl 0.869191
frigidaire 0.85677
biscuit 0.854814
maytag 0.830857
bisque 0.805774
gallery 0.788752
ge 0.783369
hotpoint 0.750769
profile 0.749047
nautilus 0.747047

Query word? kodak
easyshare 0.867683
m763 0.776361
c813 0.772292
m863 0.768097
m893 0.761642
m1063 0.746845
m341 0.745961
m381 0.745295
zx5 0.734045
m590 0.71522

Query word? ps2
ps3 0.866065
nhl 0.802828
gamecube 0.798874
2k5 0.79224
2k9 0.790914
gba 0.790538
2k6 0.788485
2k8 0.787285
2k12 0.785548
2k11 0.785374

Query word? razr
krzr 0.894957
a855 0.880824
r225 0.879094
i95cl 0.878694
i60c 0.87188
e71 0.871812
a957 0.859446
i55sr 0.85593
sgh 0.853468
i90c 0.848909

Query word? stratocaster
telecaster 0.922457
starcaster 0.889155
strat 0.841198
forecaster 0.798877
synyster 0.792257
hss 0.790215
squier 0.789585
fender 0.760396
sunburst 0.759143
fretboard 0.739114

Query word? holiday
holidays 0.978332
kwanzaa 0.864385
hanukkah 0.862716
día 0.853909
cumpleaños 0.848397
slaphappy 0.840912
congrats 0.837232
navidad 0.833956
feliz 0.833813
birthday 0.833608

Query word? plasma
600hz 0.851181
hdtvs 0.807911
tcl 0.795189
hdtv 0.79496
480hz 0.792091
xbr 0.790497
viera 0.790482
43 0.790202
58 0.789803
kuro 0.782355

Query word? leather
leatherskin 0.911778
recliner 0.705707
berkline 0.690443
armless 0.654308
hipcase 0.653687
magnolia 0.650299
theaterseatstore 0.645757
faux 0.645388
curved 0.640495
weather 0.631489

3. What fastText parameters did you use?
skipgram: epoch=25, minCount=20

4. How did you transform the product names?
Normalized the product names by converting them to lowercase, removing unusual characters, stemming. Used the provided command line script.  


## LEVEL 3: For integrating synonyms with search ##
1. How did you transform the product names (if different than previously)?
Used the same normalization as the previous step

2. What threshold score did you use?
0.75

3. Were you able to find the additional results by matching synonyms?
With the 0.75 threshold score, I actually got fewer results:
    * earbuds: without synonyms - 1205, with synonyms - 1063.
    * nespresso: without synonyms - 8, with synonyms - 8.
    * dslr: without synonyms - 2837, with synonyms - 2807.
Didn't see a significant change even on testing with a lower threshold of 0.7


