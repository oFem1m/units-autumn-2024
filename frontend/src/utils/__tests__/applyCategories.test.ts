import { applyCategories } from '../applyCategories';
import { useProducts } from '../../hooks';

describe('test applyCategories function with useProducts data', () => {
    const products = useProducts();

    it('should return all products if no categories selected', () => {
        const filteredProducts = applyCategories(products, []);
        expect(filteredProducts).toEqual(products);
    });
    it('should filter products by a single category', () => {
        const filteredProducts = applyCategories(products, ['Электроника']);
        expect(filteredProducts).toEqual([
            {
                id: 1,
                name: 'IPhone 14 Pro',
                description: 'Latest iphone, buy it now',
                price: 999,
                priceSymbol: '$',
                category: 'Электроника',
                imgUrl: '/iphone.png',
            },
            {
                id: 4,
                name: 'Принтер',
                description: 'Незаменимая вещь для студента',
                price: 7000,
                category: 'Электроника',
            },
        ]);
    });

    it('should filter products by multiple categories', () => {
        const filteredProducts = applyCategories(products, [
            'Электроника',
            'Одежда',
        ]);
        expect(filteredProducts).toEqual([
            {
                id: 1,
                name: 'IPhone 14 Pro',
                description: 'Latest iphone, buy it now',
                price: 999,
                priceSymbol: '$',
                category: 'Электроника',
                imgUrl: '/iphone.png',
            },
            {
                id: 2,
                name: 'Костюм гуся',
                description: 'Запускаем гуся, работяги',
                price: 1000,
                priceSymbol: '₽',
                category: 'Одежда',
            },
            {
                id: 4,
                name: 'Принтер',
                description: 'Незаменимая вещь для студента',
                price: 7000,
                category: 'Электроника',
            },
        ]);
    });
});
