for i in {1..10}; do
    curl -L https://cataas.com/cat -o "cat__$i.jpg"
    echo "🎁 抽到了 cat__$i.jpg"
done
open .