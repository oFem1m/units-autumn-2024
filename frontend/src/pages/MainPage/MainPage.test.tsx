import { MainPage } from './MainPage';
import { render, fireEvent } from '@testing-library/react';
import { useCurrentTime, useProducts } from '../../hooks';
import React from 'react';
import { applyCategories, updateCategories } from '../../utils';
import { Categories } from '../../components';

jest.mock('../../hooks');
jest.mock('../../utils');
jest.mock('../../components/Categories');

describe('test main page component', () => {
    afterEach(() => {
        jest.clearAllMocks();
    });
    it('shoulds contain only 1 product with category Electronics', () => {
        jest.mocked(useProducts).mockReturnValue([
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
                id: 3,
                name: 'Настольная лампа',
                description: 'Говорят, что ее использовали в pixar',
                price: 699,
                category: 'Для дома',
                imgUrl: '/lamp.png',
            },
        ]);
        jest.mocked(applyCategories).mockReturnValue([
            {
                id: 3,
                name: 'Настольная лампа',
                description: 'Говорят, что ее использовали в pixar',
                price: 699,
                category: 'Для дома',
                imgUrl: '/lamp.png',
            },
        ]);

        expect(useProducts).toHaveBeenCalledTimes(0);
        expect(applyCategories).toHaveBeenCalledTimes(0);

        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
        expect(applyCategories).toHaveBeenCalledTimes(1);
        expect(useProducts).toHaveBeenCalledTimes(1);
    });
    it('shoulds contain specified time', () => {
        jest.mocked(useCurrentTime).mockReturnValue('2020-01-01');
        expect(useCurrentTime).toHaveBeenCalledTimes(0);

        const rendered = render(<MainPage />);

        expect(useCurrentTime).toHaveBeenCalledTimes(1);
        expect(rendered.queryAllByText('2020-01-01')).toHaveLength(1);
    });
    it('shoulds click on category', () => {
        jest.mocked(updateCategories).mockReturnValue(['Для дома']);
        jest.mocked(Categories).mockImplementation(
            ({ selectedCategories, onCategoryClick }) => (
                <div key="categories">
                    <button
                        data-testid="click-me"
                        onClick={() => onCategoryClick?.('Для дома')}
                    >
                        Click me
                    </button>
                    <ul>
                        {selectedCategories.map((category) => (
                            <li key={category}>{category}</li>
                        ))}
                    </ul>
                </div>
            )
        );

        expect(updateCategories).toHaveBeenCalledTimes(0);

        const rendered = render(<MainPage />);

        expect(rendered.queryAllByText('Для дома')).toHaveLength(1);
        fireEvent.click(rendered.queryAllByTestId('click-me')[0]);
        expect(updateCategories).toHaveBeenCalledTimes(1);
        expect(updateCategories).toHaveBeenCalledWith([], 'Для дома');
        expect(rendered.queryAllByText('Для дома')).toHaveLength(2);
    });
});
