import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { getPrice } from '../../utils';

afterEach(jest.clearAllMocks);
jest.mock('../../utils');

describe('Products test', () => {
    it('should mock get price function', () => {
        jest.mocked(getPrice).mockReturnValue('100 $');

        const rendered = render(
            <ProductCard
                id={1}
                name={'Ipad'}
                description={'Ipad_description'}
                price={100}
                category={'Электроника'}
            />
        );

        expect(rendered.asFragment()).toMatchSnapshot();
        expect(getPrice).lastReturnedWith('100 $');
    });
    it('should add img by given url', () => {
        const rendered = render(
            <ProductCard
                id={1}
                name={'Ipad'}
                description={'Ipad_description'}
                price={100}
                category={'Электроника'}
                imgUrl={'public/iphone.png'}
            />
        );

        expect(rendered.asFragment()).toMatchSnapshot();
        expect(rendered.getByAltText('Ipad')).toHaveClass(
            'product-card__image'
        );
    });
    it('should not add img', () => {
        const rendered = render(
            <ProductCard
                id={12}
                name={'Table'}
                description={'Table_description'}
                price={0}
                priceSymbol={'₽'}
                category={'Для дома'}
            />
        );

        expect(rendered.asFragment()).toMatchSnapshot();
        expect(rendered.queryAllByAltText('Table')).toHaveLength(0);
    });
});
