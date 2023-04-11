import React, { useState } from 'react';

const FilmForm = (onFilmSubmit) => {
    const [filmName, setFilmName] = useState("")
    const [filmURL, setFilmURL] = useState("")

    const handleNewFilmName = event => setFilmName(event.target.value)
    const handleNewURL = event => setFilmURL(event.target.value)

    const handleSubmit = event => {
        event.preventDefault()
        const filmNameTrimmed = filmName.trim()
        const filmURLTrimmed = filmURL.trim()
        if (!filmNameTrimmed || !filmURLTrimmed) return
        onFilmSubmit({
            name: filmNameTrimmed,
            url: filmURLTrimmed,
            id: Date.now()
        })
        setFilmName("")
        setFilmURL("")}

    return ( 
        <form onSubmit={handleSubmit}>
            <input type="text" placeholder="Enter film name" onChange={handleNewFilmName} value={filmName}></input>
            <input type="text" placeholder="Enter URL from IMDB" onChange={handleNewURL} value={filmURL}></input>   
            <button>Add Film</button>    
        </form>
     );
}
 
export default FilmForm;