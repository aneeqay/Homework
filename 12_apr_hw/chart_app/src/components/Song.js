import "./Song.css"

const Song = ({chart}) => {

    const mappedChart = chart.map((song, index) => {
        return (
            <li key={index} index={index} value={index+1}>{song.title.label}</li>
        )
    })

    // const mappedChart = chart.map((song, index) => {
    //     return (
    //         <li key={index} index={index} value={index+1}>{song["im:img"]["label"]}</li>
    //     )
    // })

    return ( 
        <li className="song">{mappedChart}</li>
     );
}
 
export default Song;