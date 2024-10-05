import { updateCategories } from '../updateCategories';
import type { Category } from '../../types';

describe('test updateCategories function', () => {
    it('add a category if it dont exist', () => {
        const currentCategories: Category[] = ['Электроника', 'Для дома'];
        const newCategory: Category = 'Одежда';
        const updatedCategories = updateCategories(
            currentCategories,
            newCategory
        );
        expect(updatedCategories).toEqual([
            'Электроника',
            'Для дома',
            'Одежда',
        ]);
    });

    it('should remove a category if it already exists', () => {
        const currentCategories: Category[] = [
            'Электроника',
            'Для дома',
            'Одежда',
        ];
        const categoryToRemove: Category = 'Одежда';
        const updatedCategories = updateCategories(
            currentCategories,
            categoryToRemove
        );
        expect(updatedCategories).toEqual(['Электроника', 'Для дома']);
    });

    it('empty currentCategories array', () => {
        const currentCategories: Category[] = [];
        const newCategory: Category = 'Для дома';
        const updatedCategories = updateCategories(
            currentCategories,
            newCategory
        );
        expect(updatedCategories).toEqual(['Для дома']);
    });

    it('remove the one category if it is present', () => {
        const currentCategories: Category[] = ['Одежда'];
        const categoryToRemove: Category = 'Одежда';
        const updatedCategories = updateCategories(
            currentCategories,
            categoryToRemove
        );
        expect(updatedCategories).toEqual([]);
    });
});
