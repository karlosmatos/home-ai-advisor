import type { NextPage } from 'next';
import Head from 'next/head';
import Image from 'next/image';
import { useRef, useState } from 'react';
import { Toaster, toast } from 'react-hot-toast';
import DropDown, { IncomeType } from '../components/DropDown';
import Footer from '../components/Footer';
import Header from '../components/Header';
import LoadingDots from '../components/LoadingDots';
import Toggle from '../components/Toggle';
import { set } from 'react-hook-form';

const Home: NextPage = () => {
  const [loading, setLoading] = useState(false);
  const [lifeSituation, setLifeSituation] = useState('');
  const [income, setIncome] = useState<IncomeType>('10,000 - 25,000 CZK');
  const [generatedProperties, setGeneratedProperties] = useState<any[]>([]);
  const [generatedAIResponse, setGeneratedAIResponse] = useState<any[]>([]);
  const [isGPT, setIsGPT] = useState(false);

  const propertyRef = useRef<null | HTMLDivElement>(null);

  const scrollToProperties = () => {
    if (propertyRef.current !== null) {
      propertyRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  };

  const generateProperty = async (e: any) => {
    e.preventDefault();
    setGeneratedProperties([]);
    setLoading(true);
  
    const response = await fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/api/real_estate_recommendation/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        "life_situation": lifeSituation,
        "monthly_income_range": income
      }),
    });
  
    if (!response.ok) {
      throw new Error(response.statusText);
    }
  
    const data = await response.json();
    setGeneratedProperties(data.real_estate_list);
    setGeneratedAIResponse(data.openai_response);
    scrollToProperties();
    setLoading(false);
  };

  return (
    <div className="flex max-w-5xl mx-auto flex-col items-center justify-center py-2 min-h-screen">
      <Head>
        <title>Your AI Home Advisor</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <Header />
      <main className="flex flex-1 w-full flex-col items-center justify-center text-center px-4 mt-12 sm:mt-20">
        <p className="border rounded-2xl py-1 px-4 text-slate-500 text-sm mb-5 hover:scale-105 transition duration-300 ease-in-out">
          <b>96,434</b> happy users and counting
        </p>
        <h1 className="sm:text-6xl text-4xl max-w-[708px] font-bold text-slate-900">
          Get your new home advise based on your life situation
        </h1>
        <div className="mt-7">
          <Toggle isGPT={isGPT} setIsGPT={setIsGPT} />
        </div>

        <div className="max-w-xl w-full">
          <div className="flex mt-10 items-center space-x-3">
            <Image
              src="/1-black.png"
              width={30}
              height={30}
              alt="1 icon"
              className="mb-5 sm:mb-0"
            />
            <p className="text-left font-medium">
              Drop in your current life situation{' '}
              <span className="text-slate-500">(or your expectation)</span>.
            </p>
          </div>
          <textarea
            value={lifeSituation}
            onChange={(e) => setLifeSituation(e.target.value)}
            rows={4}
            className="w-full rounded-md border-gray-300 shadow-sm focus:border-black focus:ring-black my-5"
            placeholder={'e.g. 25 years old, single, working as a software engineer, looking for a new home to rent in Prague.'}
          />
          <div className="flex mb-5 items-center space-x-3">
            <Image src="/2-black.png" width={30} height={30} alt="1 icon" />
            <p className="text-left font-medium">Select your monthly net income.</p>
          </div>
          <div className="block">
            <DropDown income={income} setIncome={(newIncome) => setIncome(newIncome)} />
          </div>

          {!loading && (
            <button
              className="bg-black rounded-xl text-white font-medium px-4 py-2 sm:mt-10 mt-8 hover:bg-black/80 w-full"
              onClick={(e) => generateProperty(e)}
            >
              Get your dream home &rarr;
            </button>
          )}
          {loading && (
            <button
              className="bg-black rounded-xl text-white font-medium px-4 py-2 sm:mt-10 mt-8 hover:bg-black/80 w-full"
              disabled
            >
              <LoadingDots color="white" style="large" />
            </button>
          )}
        </div>
        <Toaster
          position="top-center"
          reverseOrder={false}
          toastOptions={{ duration: 2000 }}
        />
        <hr className="h-px bg-gray-700 border-1 dark:bg-gray-700" />
        <div className="space-y-10 my-10">
          {generatedAIResponse && (
            <div>
              <h2 className="sm:text-4xl text-3xl font-bold text-slate-900 mx-auto">
                AI Recommendation
              </h2>
              <p className="bg-white rounded-xl shadow-md overflow-hidden text-md mt-5 p-4">{generatedAIResponse}</p>
            </div>
          )}
          {generatedProperties && (
            <>
              <div>
                <h2
                  className="sm:text-4xl text-3xl font-bold text-slate-900 mx-auto"
                  ref={propertyRef}
                >
                  Real Estate Properties
                </h2>
              </div>
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                {generatedProperties.map((property: any) => (
                  <div
                    className="bg-white rounded-xl shadow-md overflow-hidden"
                    key={property._id.$oid}
                  >
                    <div className="relative">
                      <img
                        src={property._links.images[0].href}
                        alt={property.name}
                        className="w-full h-48 object-cover"
                      />
                      <div className="absolute top-0 right-0 bg-black text-white px-2 py-1 m-2 rounded">
                        {property.price_czk.value_raw} {property.price_czk.unit}
                      </div>
                    </div>
                    <div className="p-4">
                      <h3 className="text-xl font-semibold">{property.name}</h3>
                      <p className="text-gray-500">{property.locality}</p>
                    </div>
                  </div>
                ))}
              </div>
            </>
          )}
        </div>
      </main>
      <Footer />
    </div>
  );
};

export default Home;
