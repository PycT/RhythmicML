from RhythmicML.src.Client.UI.helpers import scanModelFolder;

test = scanModelFolder('~');

for key in test:
    print(key);
    print(test[key]);
    print();
