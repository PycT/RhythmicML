if [ ! -d "dummy" ] 
then
    mkdir dummy
fi
cd dummy
for  i in $(seq 0 37)
do 
    echo "bar$i" >> "$i.foo"
done

for i in $(seq 0 5)
do

    if [ ! -d "sub$i" ] 
    then
        mkdir sub$i
    fi

    for j in $(seq 0 12)
    do
        echo "sub-foo$i$j" >> "sub$i/$i_$j.bar"
    done
done

