import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBars, faArrowAltCircleUp } from '@fortawesome/free-solid-svg-icons';

const Response: React.FC = () => {
  const [inputValue, setInputValue] = useState('');
  const [chatHistory, setChatHistory] = useState<string[]>([]);
  const location = useLocation();
  const initialResponse = location.state?.response || "No response available";

  // Initialize chat history with the first response
  React.useEffect(() => {
    setChatHistory([`Pepper: ${initialResponse}`]);
  }, [initialResponse]);

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    try {
      const response = await fetch('http://44.243.39.185:8000/process-text/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: inputValue }),
      });

      if (response.ok) {
        const data = await response.json();
        setChatHistory(prevHistory => [
          ...prevHistory,
          `${inputValue}`,
          `Pepper: ${data.response}`
        ]);
        setInputValue(''); // Clear the input field after sending
      } else {
        console.error('Error sending message');
        setChatHistory(prevHistory => [...prevHistory, 'Error sending message']);
      }
    } catch (error) {
      console.error('Connection error:', error);
      setChatHistory(prevHistory => [...prevHistory, 'Connection error']);
    }
  };

  return (
    <div className="relative flex min-h-screen">
      <div
        className="absolute top-4 left-4 z-50 p-2 rounded-lg bg-transparent hover:bg-[#313131] transition-all duration-300"
      >
        <FontAwesomeIcon icon={faBars} className="text-white w-6 h-6 cursor-pointer" />
      </div>

      <div className="flex-1 min-h-screen overflow-y-auto overflow-x-hidden">
        <div
          className='relative flex flex-col items-center justify-center min-h-screen w-full bg-cover bg-center overflow-y-auto'
          style={{ backgroundImage: "url('/bg.png')" }}
        >
          <div className='flex flex-col items-center justify-center mx-auto mt-20 w-full'>
            {/* Display Chat History */}
            <div className="flex flex-col items-center min-h-screen text-white w-full px-4 pt-12 pb-24">
              <div className="text-center text-white w-full">
                <h1 className="text-3xl mb-24">Pepper's Response</h1>
                <div className="text-lg space-y-4 m-auto w-full px-4">
                  {chatHistory.map((message, index) => {
                    const isUser = !message.startsWith('Pepper:');
                    return (
                      <div
                        key={index}
                        className={`flex ${
                          isUser ? 'justify-end' : 'justify-start'
                        } w-full px-4`}
                      >
                        <p
                          className={`${
                            isUser
                              ? 'bg-[#2B2B2B] text-white rounded-lg p-4 ml-auto' // Added ml-auto to push user messages to the right
                              : 'bg-[#313131] text-white rounded-lg p-4'
                          } max-w-lg`}
                        >
                          {message}
                        </p>
                      </div>
                    );
                  })}
                </div>
              </div>
            </div>

            {/* Fixed Input Form at the Bottom */}
            <form
              onSubmit={handleSubmit}
              className="fixed bottom-16 w-full max-w-4xl mx-auto flex justify-center z-10 p-4 px-4" // Added px-4 for margin on both sides
            >
              <input
                type="text"
                placeholder="Converse com a Pepper"
                className="bg-[#2B2B2B] border-2 border-transparent rounded-full py-2 px-4 pr-12 text-white placeholder-gray-400 focus:outline-none hover:border-[#E3AF71] hover:border-2 transition-all duration-300 w-full"
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
              />
              <button type="submit" className="absolute top-1/2 right-4 w-4 me-4 transform -translate-y-1/2">
                <FontAwesomeIcon icon={faArrowAltCircleUp} className="text-[#222222] text-xl" />
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Response;
