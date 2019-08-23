if [ ! -d "dummy" ] 
then
    mkdir dummy
fi
cd dummy
for  i in $(seq 1 37)
do 
    echo "bar$i" >> "$i.foo"
done