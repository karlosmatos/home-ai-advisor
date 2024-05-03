import { Switch } from '@headlessui/react';
import Image from 'next/image';

function classNames(...classes: any) {
  return classes.filter(Boolean).join(' ');
}

export default function Toggle({ isLlama, setIsLlama }: any) {
  return (
    <Switch.Group as="div" className="flex items-center">
      <Switch.Label
        as="span"
        className="mr-3 text-sm flex justify-center gap-2 items-center"
      >
        <Image
          src="/mistral-logo.jpeg"
          width={25}
          height={25}
          alt="1 icon"
          className={`${isLlama && 'opacity-50'}`}
        />
        <span
          className={`font-medium ${isLlama ? 'text-gray-400' : 'text-gray-900'}`}
        >
          Mixtral
        </span>{' '}
      </Switch.Label>
      <Switch
        checked={isLlama}
        onChange={setIsLlama}
        className={classNames(
          isLlama ? 'bg-black' : 'bg-gray-200',
          'relative inline-flex h-6 w-11 flex-shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus:ring-offset-2'
        )}
      >
        <span
          aria-hidden="true"
          className={classNames(
            isLlama ? 'translate-x-5' : 'translate-x-0',
            'pointer-events-none inline-block h-5 w-5 transform rounded-full bg-white shadow ring-0 transition duration-200 ease-in-out'
          )}
        />
      </Switch>
      <Switch.Label
        as="span"
        className="ml-3 text-sm flex justify-center gap-2 items-center"
      >
        <span
          className={`font-medium ${
            !isLlama ? 'text-gray-400' : 'text-gray-900'
          }`}
        >
          Llama 3
        </span>{' '}
        <Image
          src="/meta-logo.png"
          width={30}
          height={30}
          alt="Meta logo"
          className={`${!isLlama && 'opacity-50'}`}
        />
      </Switch.Label>
    </Switch.Group>
  );
}
