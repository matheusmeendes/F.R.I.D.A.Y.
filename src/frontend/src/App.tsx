import React, { useState } from 'react';
import Card from './components/Card';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBars, faArrowAltCircleUp } from '@fortawesome/free-solid-svg-icons';

export default function App() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);
  const [inputValue, setInputValue] = useState('');
  const [response, setResponse] = useState(''); // State to hold the API response

  const chatHistory = [
    { id: 1, title: "Chat com Suporte", lastMessage: "Obrigado pela ajuda!" },
    { id: 2, title: "Chat com Vendas", lastMessage: "Qual o status do pedido?" },
    { id: 3, title: "Chat com Financeiro", lastMessage: "Enviei o comprovante." }
  ];

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    try {
      const response = await fetch('http://localhost:8000/process-text/', { // Update with your actual API endpoint
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: inputValue }), // Send inputValue as 'text'
      });

      if (response.ok) {
        const data = await response.json();
        setResponse(data.response); // Store the API response
        setInputValue(''); // Clear the input field after sending
      } else {
        console.error('Erro ao enviar a mensagem');
        setResponse('Erro ao enviar a mensagem');
      }
    } catch (error) {
      console.error('Erro na conexão com o servidor:', error);
      setResponse('Erro na conexão com o servidor');
    }
  };

  return (
    <div className="relative flex min-h-screen">
      {/* Sidebar */}
      <div 
        className={`absolute top-0 left-0 h-full bg-[#13110F] z-40 transition-all duration-300 ease-in-out ${isSidebarOpen ? 'w-1/5' : 'w-0'} overflow-hidden`}
        style={{ width: isSidebarOpen ? '20%' : '0' }} // Ensure width of sidebar
      >
        <div className="p-4">
          <h2 className="text-white text-lg mb-4">Histórico de Chats</h2>
          <ul className="space-y-2">
            {chatHistory.map((chat) => (
              <li
                key={chat.id}
                className="p-2 bg-transparent rounded-lg cursor-pointer hover:bg-[#313131] transition-all duration-300"
                onClick={() => console.log(`Clicked on ${chat.title}`)} // Example action on click
              >
                <h3 className="text-white text-sm font-semibold">{chat.title}</h3>
                <p className="text-gray-400 text-xs">{chat.lastMessage}</p>
              </li>
            ))}
          </ul>
        </div>
      </div>

      <div
        className="flex-1 transition-all duration-300 ease-in-out"
        style={{ marginLeft: isSidebarOpen ? '20%' : '0' }}
      >
        <div
          className='relative flex flex-col items-center justify-center min-h-screen bg-cover bg-center'
          style={{ backgroundImage: "url('/bg.png')" }}
        >
          <div 
            className="absolute top-4 left-4 z-50 p-2 rounded-lg bg-transparent hover:bg-[#313131] transition-all duration-300"
            onClick={() => setIsSidebarOpen(!isSidebarOpen)}
          >
            <FontAwesomeIcon icon={faBars} className="text-white w-6 h-6 cursor-pointer" />
          </div>
          <div className='flex flex-col items-center justify-center mx-auto mt-20'>
          {/* Logo and Cards */}
            <img src="/logo.svg" alt="Logo" className='mb-24' style={{ width: '94px', height: 'auto' }}/>
            <div className='space-x-8'>
              <Card text={`Tabela de\nTransações`} />
              <Card text={`Tabela de\nTransações`} />
              <Card text={`Tabela de\nTransações`} />
              <Card text={`Tabela de\nTransações`} />
            </div>

          {/* Search Input */}
            <form onSubmit={handleSubmit} className="relative w-full max-w-4xl mt-12 flex justify-center z-10">
              <input
                type="text"
                placeholder="Converse com a Pepper"
                className="bg-[#2B2B2B] border-2 border-transparent rounded-full py-2 px-4 pr-12 text-white placeholder-gray-400 focus:outline-none hover:border-[#E3AF71] hover:border-2 transition-all duration-300 w-full"
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
              />
              <button type="submit" className="absolute top-1/2 right-4 transform -translate-y-1/2">
                <FontAwesomeIcon icon={faArrowAltCircleUp} className="text-[#222222] text-xl" />
              </button>
            </form>

            {/* Display API response */}
            <div className="mt-8 text-white">
              {response && <p>{response}</p>}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
