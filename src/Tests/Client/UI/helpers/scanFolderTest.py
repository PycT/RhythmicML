from RhythmicML.src.Client.UI.helpers import scanFolder;

test = scanFolder('~');

for key in test:
    print(key);
    print(test[key]);
    print();

