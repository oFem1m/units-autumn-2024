import { useCurrentTime } from '../useCurrentTime';
import { cleanup, renderHook, act } from '@testing-library/react';

jest.mock('..');
jest.useFakeTimers();

describe('test useCurrentTime hook', () => {
    let mockToLocale: jest.SpyInstance;

    beforeEach(() => {
        mockToLocale = jest
            .spyOn(Date.prototype, 'toLocaleTimeString')
            .mockReturnValue('2020-01-01T01:00:00');
    });

    afterEach(() => {
        cleanup();
        jest.clearAllMocks();
        mockToLocale.mockRestore();
    });

    it('should return the initially mocked time', () => {
        const { result } = renderHook(() => useCurrentTime());

        expect(mockToLocale).toHaveBeenCalledTimes(1);
        expect(result.current).toEqual('2020-01-01T01:00:00');
    });

    it('should update to the newly mocked time', () => {
        const { result } = renderHook(() => useCurrentTime());

        mockToLocale.mockReturnValue('new mock locale');

        act(() => {
            jest.advanceTimersByTime(1000);
        });

        expect(mockToLocale).toHaveBeenCalledTimes(3);
        expect(result.current).toEqual('new mock locale');
    });
});
