f :: Floating a => a -> a
f x = logBase 10 (1 + 2*x) + x - 2

g' :: Fractional a => (a -> a) -> a -> a -> a
g' f a b = a - (f a * (b - a)) / (f b - f a)

hord :: (Ord t, Fractional t) => (t -> t) -> t -> t -> t -> t
hord f a b e 
    | abs (a - b) < e = b
    | otherwise = hord f b res e
    where res = g a b
          g = g' f

main = do
    presition <- getLine
    let res = hord f 0 2 (read  presition)
    print res