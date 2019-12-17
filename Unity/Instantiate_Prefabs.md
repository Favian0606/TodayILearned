# Instantiate Prefabs

## 요약
- Prefab은 GameObject를 Asset화 한것
- 복잡한 GameObject를 런타임에 인스턴스화하려는 경우 유용
- Instantiate 함수를 사용하면 런타임에 GameObject를 생성할 수 있음
	- 정확히는 해당 GameObject의 복제본을 생성하는 것
	- 복제하는 객체에 달려있는 모든 하위 객체도 포함하여 복제
	- 게임 실행 시, 해당 게임 오브젝트 옆에 (clone)이 붙어서 생성
- 보통, Instantiate로 복제하고자 하는 객체를 런타임에 실시간으로 전부 생성하지 않음
	- 미리 생성해놓고 위치 이동

## Instantiate 함수 명세

```
public static Object Instantiate(Object original, Vector3 position, Quaternion, rotation)

에디터에서 duplicate 하는 것과 유사하게 오브젝트의 클론을 원하는 위치, 회전값으로 만든다.

1. GameObject original
- 복제하려는 게임 오브젝트. 현재 scene에 있는 게임 오브젝트 또는 Prefab

2. Vector3 position
- Vector3 타입의 생성될 위치

3. Quaternion rotation
- 생성될 게임 오브젝트의 회전값
- 기본값; Quaternion.Identity
- 게임 오브젝트의 설정된 값 이용; original.transform.rotation

```

## Code Snippet

Instantiate 10 copies of a prefab object in a line along the x axis.
```cs
using UnityEngine;

public class InstantiateExample : MonoBehaviour
{
    public GameObject prefab; // Prefab GameObject

    void Start()
    {
        for (int i = 0; i < 10; i++)
        	// only x axis value is assigned by i * 2.0f
            Instantiate(prefab, new Vector3(i * 2.0f, 0, 0), Quaternion.identity);
    }
}

```

After cloning an object by Instantiate(), you can use GetComponent to set properties on a specific component attached to the cloned object.
```cs
using UnityEngine;

public class InstantiateComponentExample : MonoBehaviour
{
    // Instantiate a prefab with an attached Missile script
    public Missile missilePrefab;

    void Start()
    {
        // Instantiate the missile at the position and rotation of this object's transform
        Missile clone = (Missile)Instantiate(missilePrefab, transform.position, transform.rotation);
    }
}
```

Prefab을 Resourse.Load()로 load하여 Instantiate
```cs
using UnityEngine;

public class Board : MonoBehaviour
{

    //private Tile[,] m_TilesArray = new Tile[6, 6];
    private Dictionary<string, Tile> m_TilesDictionary = new Dictionary<string, Tile>();

    // Start is called before the first frame update
    void Start()
    {
        GameObject tilePrefab = Resources.Load("Prefabs/CandyPurple") as GameObject; // load prefab

        //Tile tile_0 = Instantiate(tilePrefab.transform.GetComponent<Tile>());
        Instantiate(tilePrefab, transform.position, transform.rotation);

        //tile_0.transform.position = Vector3.zero;
        //tile_0.transform.parent = this.transform;
    }

}

```

## 참고 페이지
- https://docs.unity3d.com/kr/530/Manual/InstantiatingPrefabs.html
- https://docs.unity3d.com/kr/530/ScriptReference/Object.Instantiate.html
- https://chameleonstudio.tistory.com/67
- https://moonpmj.tistory.com/81
- https://codingmania.tistory.com/166