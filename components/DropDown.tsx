import { Menu, Transition } from '@headlessui/react';
import {
  CheckIcon,
  ChevronDownIcon,
  ChevronUpIcon,
} from '@heroicons/react/20/solid';
import { Fragment } from 'react';

function classNames(...classes: string[]) {
  return classes.filter(Boolean).join(' ');
}

export type IncomeType = '10,000 - 25,000 CZK' | '25,000 - 40,000 CZK' | '40,000 - 60,000 CZK' | '60,000 - 80,000 CZK' | '80,000 - 100,000 CZK' | '100,000 - 150,000 CZK' | '150,000 - 200,000 CZK' | '200,000 - 300,000 CZK' | '300,000 - 500,000 CZK' | '500,000 - 1,000,000 CZK' | '1,000,000+ CZK';

interface DropDownProps {
  income: IncomeType;
  setIncome: (income: IncomeType) => void;
}

let incomes: IncomeType[] = ['10,000 - 25,000 CZK', '25,000 - 40,000 CZK', '40,000 - 60,000 CZK', '60,000 - 80,000 CZK', '80,000 - 100,000 CZK', '100,000 - 150,000 CZK', '150,000 - 200,000 CZK', '200,000 - 300,000 CZK', '300,000 - 500,000 CZK', '500,000 - 1,000,000 CZK', '1,000,000+ CZK'];

export default function DropDown({ income, setIncome }: DropDownProps) {
  return (
    <Menu as="div" className="relative block text-left w-full">
      <div>
        <Menu.Button className="inline-flex w-full justify-between items-center rounded-md border border-gray-300 bg-white px-4 py-2 text-gray-700 shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-black">
          {income}
          <ChevronUpIcon
            className="-mr-1 ml-2 h-5 w-5 ui-open:hidden"
            aria-hidden="true"
          />
          <ChevronDownIcon
            className="-mr-1 ml-2 h-5 w-5 hidden ui-open:block"
            aria-hidden="true"
          />
        </Menu.Button>
      </div>

      <Transition
        as={Fragment}
        enter="transition ease-out duration-100"
        enterFrom="transform opacity-0 scale-95"
        enterTo="transform opacity-100 scale-100"
        leave="transition ease-in duration-75"
        leaveFrom="transform opacity-100 scale-100"
        leaveTo="transform opacity-0 scale-95"
      >
        <Menu.Items
          className="absolute left-0 z-10 mt-2 w-full origin-top-right rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none"
          key={income}
        >
          <div className="">
            {incomes.map((incomeItem) => (
              <Menu.Item key={incomeItem}>
                {({ active }) => (
                  <button
                    onClick={() => setIncome(incomeItem)}
                    className={classNames(
                      active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                      income === incomeItem ? 'bg-gray-200' : '',
                      'px-4 py-2 text-sm w-full text-left flex items-center space-x-2 justify-between'
                    )}
                  >
                    <span>{incomeItem}</span>
                    {income === incomeItem ? (
                      <CheckIcon className="w-4 h-4 text-bold" />
                    ) : null}
                  </button>
                )}
              </Menu.Item>
            ))}
          </div>
        </Menu.Items>
      </Transition>
    </Menu>
  );
}
