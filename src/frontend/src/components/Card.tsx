import React from 'react'

interface CardProps {
  text: string;
}

const Card: React.FC<CardProps> = ({ text }) => {
  return (
    <div className='relative inline-flex justify-start items-end border-2 border-strokeOrange text-strokeOrange py-4 px-[120px] rounded-[20px] h-40'>
      {/* Icon at the top left */}
      <div className='absolute inset-0 bg-[#7E7E7E] opacity-0 hover:opacity-30 transition-opacity duration-500 z-0'></div>
      <div className='z-10'>
        <img 
            src="/money.svg" 
            alt="Icon" 
            className="absolute top-[4px] left-[20px] w-4 h-6 mt-6"
        />
        {/* Card text */}
        <span className='absolute left-[20px] bottom-[30px] font-light text-2xl text-left'>
          {text.split('\n').map((line, index) => (
            <React.Fragment key={index}>
              {line}
              {index < text.split('\n').length - 1 && <br />}
            </React.Fragment>
          ))}
        </span>
      </div>
    </div>
  )
}

export default Card;
